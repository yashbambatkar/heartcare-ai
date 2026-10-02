#python
# ============================================================
# HEARTCARE AI
# Professional Heart Disease Prediction System
# ============================================================

import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HeartCare AI",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROJECT PATHS
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

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "heart.csv"
)


# ============================================================
# LOAD MODEL
# ============================================================

try:

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    model_loaded = True

except Exception as e:

    model_loaded = False
    model_error = str(e)


# ============================================================
# LOAD DATASET
# ============================================================

try:

    df = pd.read_csv(DATASET_PATH)

except:

    df = None


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {

        background:
        radial-gradient(
            circle at 10% 10%,
            rgba(59,130,246,0.10),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(239,68,68,0.09),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #06101d,
            #081522,
            #050c16
        );

        color: #f8fafc;
    }


    .block-container {

        max-width: 1450px;

        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* =====================================================
       REMOVE STREAMLIT HEADER
       ===================================================== */

    header[data-testid="stHeader"] {

        background: transparent;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #030914,
            #071423
        );

        border-right:
        1px solid rgba(255,255,255,0.08);
    }


    .sidebar-logo {

        text-align: center;

        padding: 15px 0 28px 0;
    }


    .sidebar-heart {

        width: 72px;
        height: 72px;

        margin: auto;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 22px;

        font-size: 38px;

        background:
        linear-gradient(
            135deg,
            rgba(239,68,68,0.20),
            rgba(239,68,68,0.05)
        );

        border:
        1px solid rgba(239,68,68,0.25);

        box-shadow:
        0 10px 35px rgba(239,68,68,0.12);
    }


    .sidebar-title {

        font-size: 25px;

        font-weight: 850;

        color: #ffffff;

        margin-top: 13px;
    }


    .sidebar-subtitle {

        color: #718096;

        font-size: 12px;

        margin-top: 4px;
    }


    /* =====================================================
       HERO
       ===================================================== */

    .hero {

        position: relative;

        overflow: hidden;

        padding: 60px;

        border-radius: 30px;

        margin-bottom: 30px;

        background:
        linear-gradient(
            135deg,
            rgba(15,34,58,0.98),
            rgba(8,22,39,0.94)
        );

        border:
        1px solid rgba(255,255,255,0.10);

        box-shadow:
        0 30px 80px rgba(0,0,0,0.38);
    }


    .hero::before {

        content: "";

        position: absolute;

        width: 420px;
        height: 420px;

        border-radius: 50%;

        right: -170px;
        top: -180px;

        background:
        radial-gradient(
            circle,
            rgba(239,68,68,0.18),
            transparent 68%
        );
    }


    .hero::after {

        content: "❤";

        position: absolute;

        right: 75px;
        top: 45px;

        font-size: 120px;

        opacity: 0.06;
    }


    .hero-badge {

        display: inline-block;

        padding: 8px 16px;

        border-radius: 30px;

        background:
        rgba(59,130,246,0.10);

        border:
        1px solid rgba(59,130,246,0.25);

        color: #93c5fd;

        font-size: 12px;

        font-weight: 700;

        letter-spacing: 1px;

        margin-bottom: 20px;
    }


    .hero-title {

        position: relative;

        font-size: 56px;

        line-height: 1.08;

        font-weight: 900;

        letter-spacing: -2px;

        margin-bottom: 20px;
    }


    .hero-title span {

        background:
        linear-gradient(
            90deg,
            #fb7185,
            #ef4444
        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }


    .hero-description {

        position: relative;

        max-width: 780px;

        color: #9fb0c3;

        font-size: 17px;

        line-height: 1.75;
    }


    /* =====================================================
       SECTION
       ===================================================== */

    .section-title {

        font-size: 27px;

        font-weight: 800;

        margin-top: 28px;

        margin-bottom: 5px;

        color: #f8fafc;
    }


    .section-description {

        color: #718096;

        margin-bottom: 22px;

        font-size: 14px;
    }


    /* =====================================================
       METRICS
       ===================================================== */

    .metric {

        position: relative;

        overflow: hidden;

        background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.065),
            rgba(255,255,255,0.025)
        );

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius: 20px;

        padding: 25px;

        min-height: 125px;

        transition: 0.25s ease;
    }


    .metric:hover {

        transform: translateY(-4px);

        border-color:
        rgba(255,255,255,0.16);

        box-shadow:
        0 18px 45px rgba(0,0,0,0.25);
    }


    .metric-icon {

        font-size: 22px;

        margin-bottom: 12px;
    }


    .metric-value {

        font-size: 30px;

        font-weight: 850;

        color: #ffffff;
    }


    .metric-label {

        color: #718096;

        font-size: 12px;

        margin-top: 5px;
    }


    /* =====================================================
       CARDS
       ===================================================== */

    .card {

        background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.055),
            rgba(255,255,255,0.025)
        );

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius: 22px;

        padding: 28px;

        margin-bottom: 22px;

        box-shadow:
        0 15px 45px rgba(0,0,0,0.16);
    }


    .card-heading {

        font-size: 20px;

        font-weight: 750;

        color: #ffffff;

        margin-bottom: 9px;
    }


    .card-text {

        color: #91a1b5;

        line-height: 1.75;

        font-size: 14px;
    }


    /* =====================================================
       INPUT SECTIONS
       ===================================================== */

    .input-header {

        padding: 20px 23px;

        border-radius: 17px;

        background:
        linear-gradient(
            90deg,
            rgba(59,130,246,0.08),
            rgba(255,255,255,0.025)
        );

        border:
        1px solid rgba(255,255,255,0.07);

        margin-top: 25px;

        margin-bottom: 18px;
    }


    .input-header-title {

        font-size: 18px;

        font-weight: 750;

        color: #ffffff;
    }


    .input-header-subtitle {

        color: #718096;

        font-size: 12px;

        margin-top: 4px;
    }


    /* =====================================================
       STREAMLIT INPUTS
       ===================================================== */

    div[data-baseweb="select"] > div {

        background-color:
        rgba(255,255,255,0.045);

        border-color:
        rgba(255,255,255,0.10);
    }


    div[data-testid="stNumberInput"] input {

        background:
        rgba(255,255,255,0.045);

        color: #ffffff;

        border:
        1px solid rgba(255,255,255,0.10);

        border-radius: 10px;
    }


    label {

        color: #b5c1cf !important;

        font-size: 13px !important;
    }


    /* =====================================================
       MAIN BUTTON
       ===================================================== */

    div.stButton > button {

        width: 100%;

        height: 60px;

        border-radius: 15px;

        border: none;

        color: #ffffff;

        font-size: 16px;

        font-weight: 800;

        background:
        linear-gradient(
            90deg,
            #dc2626,
            #ef4444,
            #f43f5e
        );

        box-shadow:
        0 12px 35px rgba(239,68,68,0.22);

        transition: all 0.25s ease;
    }


    div.stButton > button:hover {

        transform:
        translateY(-3px);

        box-shadow:
        0 18px 45px rgba(239,68,68,0.35);
    }


    /* =====================================================
       RESULT
       ===================================================== */

    .result {

        position: relative;

        overflow: hidden;

        padding: 45px;

        border-radius: 28px;

        text-align: center;

        margin-top: 35px;

        background:
        linear-gradient(
            145deg,
            rgba(239,68,68,0.14),
            rgba(255,255,255,0.035)
        );

        border:
        1px solid rgba(239,68,68,0.22);

        box-shadow:
        0 25px 70px rgba(0,0,0,0.30);
    }


    .result-icon {

        font-size: 45px;

        margin-bottom: 8px;
    }


    .result-label {

        color: #94a3b8;

        font-size: 11px;

        font-weight: 700;

        letter-spacing: 2px;
    }


    .result-title {

        font-size: 45px;

        font-weight: 900;

        color: #fb7185;

        margin: 10px 0;
    }


    .result-probability {

        font-size: 18px;

        color: #cbd5e1;
    }


    /* =====================================================
       PIPELINE
       ===================================================== */

    .pipeline {

        display: flex;

        justify-content: space-between;

        align-items: center;

        gap: 10px;

        padding: 28px;

        background:
        rgba(255,255,255,0.035);

        border-radius: 20px;

        border:
        1px solid rgba(255,255,255,0.07);
    }


    .pipeline-step {

        text-align: center;

        flex: 1;

        color: #cbd5e1;

        font-size: 13px;
    }


    .pipeline-number {

        width: 45px;

        height: 45px;

        margin: auto auto 10px auto;

        border-radius: 50%;

        display: flex;

        align-items: center;

        justify-content: center;

        background:
        rgba(59,130,246,0.12);

        border:
        1px solid rgba(59,130,246,0.30);

        color: #93c5fd;

        font-weight: 800;
    }


    .pipeline-arrow {

        color: #475569;

        font-size: 22px;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {

        margin-top: 70px;

        padding-top: 25px;

        text-align: center;

        color: #64748b;

        font-size: 12px;

        border-top:
        1px solid rgba(255,255,255,0.07);
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 800px) {

        .hero {

            padding: 32px;
        }

        .hero-title {

            font-size: 37px;
        }

        .hero-description {

            font-size: 15px;
        }

        .pipeline {

            flex-direction: column;
        }

        .pipeline-arrow {

            transform: rotate(90deg);
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">

            <div class="sidebar-heart">
                ❤️
            </div>

            <div class="sidebar-title">
                HeartCare AI
            </div>

            <div class="sidebar-subtitle">
                Intelligent Health Analytics
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "WORKSPACE",
        [
            "Dashboard",
            "Prediction",
            "Model Lab",
            "Project"
        ]
    )

    st.markdown("---")

    st.caption("ARTIFICIAL INTELLIGENCE")
    st.caption("Machine Learning")
    st.caption("Academic Project • 2026")


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                ARTIFICIAL INTELLIGENCE • HEALTH ANALYTICS
            </div>

            <div class="hero-title">
                Intelligent <span>Heart Health</span><br>
                Analysis Platform
            </div>

            <div class="hero-description">
                HeartCare AI demonstrates an end-to-end
                machine-learning workflow for analyzing
                structured health data and generating
                classification predictions.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # METRICS
    # ========================================================

    dataset_rows = len(df) if df is not None else 302

    col1, col2, col3, col4 = st.columns(4)

    metrics = [

        ("🧬", "13", "Input Features"),

        ("📊", str(dataset_rows), "Dataset Records"),

        ("🎯", "80.33%", "Test Accuracy"),

        ("🤖", "3", "Models Evaluated")

    ]


    for column, metric in zip(
        [col1, col2, col3, col4],
        metrics
    ):

        icon, value, label = metric

        with column:

            st.markdown(
                f"""
                <div class="metric">

                    <div class="metric-icon">
                        {icon}
                    </div>

                    <div class="metric-value">
                        {value}
                    </div>

                    <div class="metric-label">
                        {label}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # ABOUT
    # ========================================================

    col1, col2 = st.columns([1.15, 0.85])

    with col1:

        st.markdown(
            """
            <div class="card">

                <div class="card-heading">
                    ❤️ What is HeartCare AI?
                </div>

                <div class="card-text">

                    HeartCare AI is an academic machine-learning
                    application designed to demonstrate the
                    complete workflow of a predictive analytics
                    system.

                    <br><br>

                    The system takes structured health-related
                    input data, applies the same preprocessing
                    used during model development and generates
                    a classification prediction.

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class="card">

                <div class="card-heading">
                    ⚙️ Technology Stack
                </div>

                <div class="card-text">

                    <b>Python</b><br>
                    Application development

                    <br><br>

                    <b>Pandas & NumPy</b><br>
                    Data processing

                    <br><br>

                    <b>Scikit-learn</b><br>
                    Machine learning

                    <br><br>

                    <b>Streamlit</b><br>
                    Interactive web application

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # PIPELINE
    # ========================================================

    st.markdown(
        '<div class="section-title">Machine Learning Pipeline</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'From raw data to an interactive prediction.'
        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="pipeline">

            <div class="pipeline-step">

                <div class="pipeline-number">
                    01
                </div>

                Dataset

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    02
                </div>

                Preprocessing

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    03
                </div>

                Training

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    04
                </div>

                Evaluation

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    05
                </div>

                Prediction

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="footer">

            <b>HeartCare AI</b>
            &nbsp; • &nbsp;
            Intelligent Health Analytics

            <br><br>

            Machine Learning Academic Project
            &nbsp; • &nbsp;
            Educational Use Only

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PREDICTION PAGE
# ============================================================

elif page == "Prediction":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                AI PREDICTION WORKSPACE
            </div>

            <div class="hero-title">
                Patient <span>Assessment</span>
            </div>

            <div class="hero-description">
                Enter the 13 input features required by the
                trained classification model.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    if not model_loaded:

        st.error(
            "Model files could not be loaded."
        )

        st.code(model_error)

        st.stop()


    # ========================================================
    # BASIC INFORMATION
    # ========================================================

    st.markdown(
        """
        <div class="input-header">

            <div class="input-header-title">
                👤 Basic Information
            </div>

            <div class="input-header-subtitle">
                Demographic and symptom information
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=50
        )


    with col2:

        sex = st.selectbox(
            "Sex",
            [0, 1],
            format_func=lambda x:
            "Female" if x == 0 else "Male"
        )


    with col3:

        cp = st.selectbox(
            "Chest Pain Type",
            [0, 1, 2, 3]
        )


    # ========================================================
    # CLINICAL INFORMATION
    # ========================================================

    st.markdown(
        """
        <div class="input-header">

            <div class="input-header-title">
                🩺 Clinical Measurements
            </div>

            <div class="input-header-subtitle">
                Cardiovascular measurement inputs
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        trestbps = st.number_input(
            "Resting Blood Pressure",
            min_value=50,
            max_value=250,
            value=120
        )


    with col2:

        chol = st.number_input(
            "Cholesterol",
            min_value=50,
            max_value=700,
            value=200
        )


    with col3:

        thalach = st.number_input(
            "Maximum Heart Rate",
            min_value=50,
            max_value=250,
            value=150
        )


    # ========================================================
    # ADDITIONAL FEATURES
    # ========================================================

    st.markdown(
        """
        <div class="input-header">

            <div class="input-header-title">
                📋 Additional Model Features
            </div>

            <div class="input-header-subtitle">
                Variables required by the trained model
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        fbs = st.selectbox(
            "Fasting Blood Sugar",
            [0, 1],
            format_func=lambda x:
            "No" if x == 0 else "Yes"
        )


    with col2:

        restecg = st.selectbox(
            "Resting ECG",
            [0, 1, 2]
        )


    with col3:

        exang = st.selectbox(
            "Exercise-Induced Angina",
            [0, 1],
            format_func=lambda x:
            "No" if x == 0 else "Yes"
        )


    col1, col2, col3 = st.columns(3)


    with col1:

        oldpeak = st.number_input(
            "ST Depression",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=0.1
        )


    with col2:

        slope = st.selectbox(
            "Slope",
            [0, 1, 2]
        )


    with col3:

        ca = st.selectbox(
            "Major Vessels",
            [0, 1, 2, 3]
        )


    thal = st.selectbox(
        "Thal",
        [0, 1, 2, 3]
    )


    st.write("")


    # ========================================================
    # PREDICT BUTTON
    # ========================================================

    predict = st.button(
        "❤️  ANALYZE PATIENT DATA"
    )


    if predict:

        input_data = pd.DataFrame({

            "age": [age],
            "sex": [sex],
            "cp": [cp],
            "trestbps": [trestbps],
            "chol": [chol],
            "fbs": [fbs],
            "restecg": [restecg],
            "thalach": [thalach],
            "exang": [exang],
            "oldpeak": [oldpeak],
            "slope": [slope],
            "ca": [ca],
            "thal": [thal]

        })


        # ----------------------------------------------------
        # PREPROCESS
        # ----------------------------------------------------

        input_scaled = scaler.transform(
            input_data
        )


        # ----------------------------------------------------
        # PREDICTION
        # ----------------------------------------------------

        prediction = model.predict(
            input_scaled
        )[0]


        probabilities = model.predict_proba(
            input_scaled
        )[0]


        probability = (
            probabilities[prediction] * 100
        )


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        if prediction == 1:

            result_title = "Class 1 Detected"
            result_icon = "⚠️"

        else:

            result_title = "Class 0 Detected"
            result_icon = "✓"


        st.markdown(
            f"""
            <div class="result">

                <div class="result-icon">
                    {result_icon}
                </div>

                <div class="result-label">
                    MODEL ANALYSIS COMPLETE
                </div>

                <div class="result-title">
                    {result_title}
                </div>

                <div class="result-probability">

                    Model confidence:
                    <b>{probability:.2f}%</b>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")

        st.progress(
            min(int(probability), 100)
        )


        if prediction == 1:

            st.warning(
                "The trained model classified this input "
                "as class 1."
            )

        else:

            st.success(
                "The trained model classified this input "
                "as class 0."
            )


        st.info(
            "This is a machine-learning classification result "
            "from an academic project. It is not a medical "
            "diagnosis and should not be used for clinical "
            "decision-making."
        )


# ============================================================
# MODEL LAB
# ============================================================

elif page == "Model Lab":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                MACHINE LEARNING LAB
            </div>

            <div class="hero-title">
                Model <span>Performance</span>
            </div>

            <div class="hero-description">
                Evaluation results from the classification
                models developed during the project.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # METRICS
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)


    model_metrics = [

        ("Accuracy", "80.33%"),

        ("Precision", "80.00%"),

        ("Recall", "84.85%"),

        ("F1 Score", "82.35%")

    ]


    for column, (label, value) in zip(
        [col1, col2, col3, col4],
        model_metrics
    ):

        with column:

            st.markdown(
                f"""
                <div class="metric">

                    <div class="metric-value">
                        {value}
                    </div>

                    <div class="metric-label">
                        {label}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # MODEL COMPARISON
    # ========================================================

    st.markdown(
        '<div class="section-title">Model Comparison</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Evaluation metrics obtained during model testing.'
        '</div>',
        unsafe_allow_html=True
    )


    comparison = pd.DataFrame({

        "Model": [

            "Logistic Regression",

            "Decision Tree",

            "Random Forest"

        ],

        "Accuracy": [

            0.8033,

            0.8033,

            0.7541

        ],

        "Precision": [

            0.8000,

            0.8182,

            0.7647

        ],

        "Recall": [

            0.8485,

            0.8182,

            0.7879

        ],

        "F1 Score": [

            0.8235,

            0.8182,

            0.7761

        ]

    })


    st.dataframe(
        comparison.style.format({
            "Accuracy": "{:.2%}",
            "Precision": "{:.2%}",
            "Recall": "{:.2%}",
            "F1 Score": "{:.2%}"
        }),
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # FEATURE IMPORTANCE
    # ========================================================

    st.markdown(
        '<div class="section-title">Model Feature Coefficients</div>',
        unsafe_allow_html=True
    )


    if hasattr(model, "coef_"):

        feature_names = [

            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal"

        ]


        coefficients = np.abs(
            model.coef_[0]
        )


        importance_df = pd.DataFrame({

            "Feature": feature_names,

            "Importance": coefficients

        }).sort_values(
            "Importance",
            ascending=False
        )


        st.bar_chart(
            importance_df.set_index(
                "Feature"
            )
        )


    st.caption(
        "Model coefficients describe the trained model's "
        "relationship with its input features. They should "
        "not be interpreted as medical causation."
    )


# ============================================================
# PROJECT PAGE
# ============================================================

elif page == "Project":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                FINAL YEAR PROJECT
            </div>

            <div class="hero-title">
                HeartCare <span>AI</span>
            </div>

            <div class="hero-description">
                An end-to-end machine-learning application
                demonstrating data preprocessing, model
                development, evaluation and interactive
                deployment.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            """
            <div class="card">

                <div class="card-heading">
                    🎯 Project Objective
                </div>

                <div class="card-text">

                    Develop an interactive machine-learning
                    application that accepts structured
                    health-related input data and generates
                    a classification prediction.

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class="card">

                <div class="card-heading">
                    🧠 Machine Learning
                </div>

                <div class="card-text">

                    The project evaluates multiple classification
                    algorithms including Logistic Regression,
                    Decision Tree and Random Forest.

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="section-title">Project Architecture</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="pipeline">

            <div class="pipeline-step">

                <div class="pipeline-number">
                    01
                </div>

                Dataset

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    02
                </div>

                Preprocessing

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    03
                </div>

                ML Models

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    04
                </div>

                Evaluation

            </div>

            <div class="pipeline-arrow">→</div>

            <div class="pipeline-step">

                <div class="pipeline-number">
                    05
                </div>

                Streamlit

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    st.markdown(
        """
        <div class="card">

            <div class="card-heading">
                🛠️ Technology Stack
            </div>

            <div class="card-text">

                Python
                &nbsp; • &nbsp;

                Pandas
                &nbsp; • &nbsp;

                NumPy
                &nbsp; • &nbsp;

                Scikit-learn
                &nbsp; • &nbsp;

                Joblib
                &nbsp; • &nbsp;

                Streamlit

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.warning(
        "HeartCare AI is an academic and educational "
        "machine-learning demonstration. It is not intended "
        "for diagnosis, treatment or clinical decision-making."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <b>HeartCare AI</b>
        &nbsp; • &nbsp;
        Intelligent Health Analytics

        <br><br>

        Machine Learning Academic Project
        &nbsp; • &nbsp;
        Educational Use Only

    </div>
    """,
    unsafe_allow_html=True
)
