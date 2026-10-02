import { useState } from "react";
import {
  HeartPulse,
  Activity,
  ShieldCheck,
  Brain,
  ArrowRight,
  RotateCcw,
  UserRound,
  Stethoscope,
  CheckCircle2,
  AlertCircle,
} from "lucide-react";
import "./index.css";

function App() {
  const [formData, setFormData] = useState({
    age: 50,
    sex: 1,
    cp: 0,
    trestbps: 120,
    chol: 200,
    fbs: 0,
    restecg: 0,
    thalach: 150,
    exang: 0,
    oldpeak: 1,
    slope: 1,
    ca: 0,
    thal: 2,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: Number(value),
    });
  };

  const handleReset = () => {
    setFormData({
      age: 50,
      sex: 1,
      cp: 0,
      trestbps: 120,
      chol: 200,
      fbs: 0,
      restecg: 0,
      thalach: 150,
      exang: 0,
      oldpeak: 1,
      slope: 1,
      ca: 0,
      thal: 2,
    });

    setResult(null);
  };

  const handlePredict = async () => {
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Prediction request failed");
      }

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error(error);

      setResult({
        error:
          "Unable to connect to the backend. Make sure your FastAPI server is running.",
      });
    }

    setLoading(false);
  };

  return (
    <div className="app">

      {/* NAVBAR */}

      <nav className="navbar">

        <div className="logo">
          <div className="logo-icon">
            <HeartPulse size={25} />
          </div>

          <div>
            <h2>HeartCare AI</h2>
            <span>Intelligent Health Analytics</span>
          </div>
        </div>

        <div className="nav-status">
          <span className="status-dot"></span>
          AI System Online
        </div>

      </nav>


      {/* HERO */}

      <section className="hero">

        <div className="hero-content">

          <div className="badge">
            <Brain size={16} />
            ARTIFICIAL INTELLIGENCE • HEALTH ANALYTICS
          </div>

          <h1>
            Intelligent{" "}
            <span>Heart Health</span>
            <br />
            Analysis Platform
          </h1>

          <p>
            An interactive machine-learning platform that analyzes
            structured health information and generates a classification
            prediction using a trained artificial intelligence model.
          </p>

          <div className="hero-buttons">

            <button
              className="primary-button"
              onClick={() =>
                document
                  .getElementById("prediction")
                  .scrollIntoView({ behavior: "smooth" })
              }
            >
              Start Analysis
              <ArrowRight size={18} />
            </button>

            <button
              className="secondary-button"
              onClick={() =>
                document
                  .getElementById("about")
                  .scrollIntoView({ behavior: "smooth" })
              }
            >
              Learn More
            </button>

          </div>

        </div>


        <div className="hero-card">

          <div className="heart-animation">
            <HeartPulse size={75} />
          </div>

          <h3>HeartCare AI</h3>

          <p>
            Machine Learning Prediction System
          </p>

          <div className="mini-stats">

            <div>
              <strong>13</strong>
              <span>Features</span>
            </div>

            <div>
              <strong>302</strong>
              <span>Records</span>
            </div>

            <div>
              <strong>80.33%</strong>
              <span>Accuracy</span>
            </div>

          </div>

        </div>

      </section>


      {/* FEATURES */}

      <section className="features" id="about">

        <div className="section-heading">

          <span>PLATFORM CAPABILITIES</span>

          <h2>
            Built for intelligent health analysis
          </h2>

          <p>
            A complete machine-learning workflow from patient
            input to model prediction.
          </p>

        </div>


        <div className="feature-grid">

          <div className="feature-card">

            <div className="feature-icon">
              <Brain />
            </div>

            <h3>Machine Learning</h3>

            <p>
              Uses a trained classification model to analyze
              structured health-related features.
            </p>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              <Activity />
            </div>

            <h3>Health Analytics</h3>

            <p>
              Processes multiple cardiovascular measurements
              to generate a model-based prediction.
            </p>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              <ShieldCheck />
            </div>

            <h3>Educational System</h3>

            <p>
              Designed as an academic demonstration of an
              end-to-end machine-learning application.
            </p>

          </div>

        </div>

      </section>


      {/* PREDICTION */}

      <section className="prediction-section" id="prediction">

        <div className="section-heading">

          <span>AI PREDICTION WORKSPACE</span>

          <h2>Patient Assessment</h2>

          <p>
            Enter the required features and send them to the
            machine-learning backend.
          </p>

        </div>


        <div className="prediction-container">

          <div className="form-card">

            <div className="form-title">

              <div className="form-icon">
                <UserRound />
              </div>

              <div>
                <h3>Patient Information</h3>
                <p>Enter cardiovascular measurements</p>
              </div>

            </div>


            <div className="form-grid">

              <div className="input-group">
                <label>Age</label>

                <input
                  type="number"
                  name="age"
                  value={formData.age}
                  onChange={handleChange}
                />
              </div>


              <div className="input-group">
                <label>Sex</label>

                <select
                  name="sex"
                  value={formData.sex}
                  onChange={handleChange}
                >
                  <option value={0}>Female</option>
                  <option value={1}>Male</option>
                </select>
              </div>


              <div className="input-group">
                <label>Chest Pain Type</label>

                <select
                  name="cp"
                  value={formData.cp}
                  onChange={handleChange}
                >
                  <option value={0}>Type 0</option>
                  <option value={1}>Type 1</option>
                  <option value={2}>Type 2</option>
                  <option value={3}>Type 3</option>
                </select>
              </div>


              <div className="input-group">
                <label>Resting Blood Pressure</label>

                <input
                  type="number"
                  name="trestbps"
                  value={formData.trestbps}
                  onChange={handleChange}
                />
              </div>


              <div className="input-group">
                <label>Cholesterol</label>

                <input
                  type="number"
                  name="chol"
                  value={formData.chol}
                  onChange={handleChange}
                />
              </div>


              <div className="input-group">
                <label>Maximum Heart Rate</label>

                <input
                  type="number"
                  name="thalach"
                  value={formData.thalach}
                  onChange={handleChange}
                />
              </div>


              <div className="input-group">
                <label>Fasting Blood Sugar</label>

                <select
                  name="fbs"
                  value={formData.fbs}
                  onChange={handleChange}
                >
                  <option value={0}>No</option>
                  <option value={1}>Yes</option>
                </select>
              </div>


              <div className="input-group">
                <label>Resting ECG</label>

                <select
                  name="restecg"
                  value={formData.restecg}
                  onChange={handleChange}
                >
                  <option value={0}>Type 0</option>
                  <option value={1}>Type 1</option>
                  <option value={2}>Type 2</option>
                </select>
              </div>


              <div className="input-group">
                <label>Exercise-Induced Angina</label>

                <select
                  name="exang"
                  value={formData.exang}
                  onChange={handleChange}
                >
                  <option value={0}>No</option>
                  <option value={1}>Yes</option>
                </select>
              </div>


              <div className="input-group">
                <label>ST Depression</label>

                <input
                  type="number"
                  step="0.1"
                  name="oldpeak"
                  value={formData.oldpeak}
                  onChange={handleChange}
                />
              </div>


              <div className="input-group">
                <label>Slope</label>

                <select
                  name="slope"
                  value={formData.slope}
                  onChange={handleChange}
                >
                  <option value={0}>Type 0</option>
                  <option value={1}>Type 1</option>
                  <option value={2}>Type 2</option>
                </select>
              </div>


              <div className="input-group">
                <label>Major Vessels</label>

                <select
                  name="ca"
                  value={formData.ca}
                  onChange={handleChange}
                >
                  <option value={0}>0</option>
                  <option value={1}>1</option>
                  <option value={2}>2</option>
                  <option value={3}>3</option>
                </select>
              </div>


              <div className="input-group">
                <label>Thal</label>

                <select
                  name="thal"
                  value={formData.thal}
                  onChange={handleChange}
                >
                  <option value={0}>Type 0</option>
                  <option value={1}>Type 1</option>
                  <option value={2}>Type 2</option>
                  <option value={3}>Type 3</option>
                </select>
              </div>

            </div>


            <div className="form-buttons">

              <button
                className="reset-button"
                onClick={handleReset}
              >
                <RotateCcw size={17} />
                Reset
              </button>

              <button
                className="predict-button"
                onClick={handlePredict}
                disabled={loading}
              >
                <HeartPulse size={18} />

                {loading
                  ? "Analyzing..."
                  : "Analyze Patient Data"}
              </button>

            </div>

          </div>


          {/* RESULT */}

          <div className="result-card">

            <div className="result-header">

              <div className="result-icon">
                <Stethoscope />
              </div>

              <div>
                <h3>AI Analysis</h3>
                <p>Prediction result</p>
              </div>

            </div>


            {!result && (

              <div className="empty-result">

                <HeartPulse size={55} />

                <h3>Ready for Analysis</h3>

                <p>
                  Enter patient information and click
                  <strong> Analyze Patient Data</strong>.
                </p>

              </div>

            )}


            {result && !result.error && (

              <div className="prediction-result">

                {result.prediction === 1 ? (
                  <AlertCircle className="result-large-icon" />
                ) : (
                  <CheckCircle2 className="result-large-icon" />
                )}

                <span className="result-label">
                  MODEL PREDICTION
                </span>

                <h2>
                  Class {result.prediction}
                </h2>

                <div className="probability">
                  {Number(result.probability).toFixed(2)}%
                </div>

                <p>
                  Model probability for the predicted class
                </p>

              </div>

            )}


            {result?.error && (

              <div className="backend-error">

                <AlertCircle size={45} />

                <h3>Backend Connection Error</h3>

                <p>
                  {result.error}
                </p>

              </div>

            )}

          </div>

        </div>

      </section>


      {/* PIPELINE */}

      <section className="pipeline-section">

        <div className="section-heading">

          <span>MACHINE LEARNING WORKFLOW</span>

          <h2>From data to prediction</h2>

        </div>


        <div className="pipeline">

          <div>
            <strong>01</strong>
            <span>Dataset</span>
          </div>

          <ArrowRight />

          <div>
            <strong>02</strong>
            <span>Preprocessing</span>
          </div>

          <ArrowRight />

          <div>
            <strong>03</strong>
            <span>Model Training</span>
          </div>

          <ArrowRight />

          <div>
            <strong>04</strong>
            <span>Evaluation</span>
          </div>

          <ArrowRight />

          <div>
            <strong>05</strong>
            <span>Prediction</span>
          </div>

        </div>

      </section>


      {/* FOOTER */}

      <footer>

        <div className="footer-logo">
          <HeartPulse size={22} />
          <strong>HeartCare AI</strong>
        </div>

        <p>
          Intelligent Health Analytics • Machine Learning Academic Project
        </p>

        <small>
          Educational demonstration only. This application is not a
          medical diagnostic system.
        </small>

      </footer>

    </div>
  );
}

export default App;