
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="HeartCare AI API",
    description="Heart Disease Prediction Backend",
    version="1.0.0"
)

# ============================================================
# CORS CONFIGURATION
# ============================================================


ALLOWED_ORIGINS = [
    "https://heartcare-ai-psi.vercel.app",
    "https://heartcare-p7weuxyot-yash-f638.vercel.app",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# ============================================================
# MODEL AND SCALER PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "heart_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR, "models", "scaler.pkl"
)

# ============================================================
# LOAD MODEL AND SCALER
# ============================================================

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# ============================================================
# INPUT DATA
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
# HOME ENDPOINT
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
# PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict(data: PatientData):

    input_data = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "cp": data.cp,
        "trestbps": data.trestbps,
        "chol": data.chol,
        "fbs": data.fbs,
        "restecg": data.restecg,
        "thalach": data.thalach,
        "exang": data.exang,
        "oldpeak": data.oldpeak,
        "slope": data.slope,
        "ca": data.ca,
        "thal": data.thal,
    }])

    input_scaled = scaler.transform(input_data)

    prediction = int(model.predict(input_scaled)[0])

    probabilities = model.predict_proba(input_scaled)[0]
    probability = float(probabilities[prediction]) * 100

    return {
        "prediction": prediction,
        "probability": round(probability, 2)
    }
