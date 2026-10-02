
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import os


# ============================================================
# CREATE FASTAPI APP
# ============================================================

app = FastAPI(
    title="HeartCare AI API",
    description="Heart Disease Prediction Backend",
    version="1.0"
)


# ============================================================
# CORS CONFIGURATION
# ============================================================

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://heartcare-p7weuxyot-yash-f638.vercel.app",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# MODEL PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "heart_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)


# ============================================================
# LOAD MODEL AND SCALER
# ============================================================

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# ============================================================
# INPUT DATA STRUCTURE
# ============================================================

class PatientData(BaseModel):

    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "HeartCare AI Backend is working!"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "HeartCare AI API"
    }


# ============================================================
# PREDICTION
# ============================================================

@app.post("/predict")
def predict(data: PatientData):

    input_data = pd.DataFrame({

        "age": [data.age],
        "sex": [data.sex],
        "cp": [data.cp],
        "trestbps": [data.trestbps],
        "chol": [data.chol],
        "fbs": [data.fbs],
        "restecg": [data.restecg],
        "thalach": [data.thalach],
        "exang": [data.exang],
        "oldpeak": [data.oldpeak],
        "slope": [data.slope],
        "ca": [data.ca],
        "thal": [data.thal]

    })


    # ========================================================
    # SCALE INPUT
    # ========================================================

    input_scaled = scaler.transform(input_data)


    # ========================================================
    # MODEL PREDICTION
    # ========================================================

    prediction = model.predict(
        input_scaled
    )[0]


    # ========================================================
    # PREDICTION PROBABILITY
    # ========================================================

    probabilities = model.predict_proba(
        input_scaled
    )[0]

    probability = (
        probabilities[int(prediction)] * 100
    )


    # ========================================================
    # RESPONSE
    # ========================================================

    return {

        "prediction": int(prediction),

        "probability": round(
            float(probability),
            2
        )

    }
