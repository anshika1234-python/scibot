# populate_data.py
import os
os.makedirs("data", exist_ok=True)

docs = {
    "mechanics_overview.txt": """Mechanics — Overview
Classical mechanics studies motion, forces, energy and momentum.
Key equations:
- Newton's second law: F = m a
- Kinetic energy: K = 1/2 m v^2
- Conservation of energy and momentum are core principles.
Dimensional analysis helps check formula correctness.
""",

    "electronics_basics.txt": """Electronics — Basics
Circuit elements: resistor, capacitor, inductor.
Ohm's law: V = I R.
RC time constant: tau = R C.
Operational amplifiers: ideal op-amp assumptions used in analog design.
Signal conditioning and filters are common practical tasks.
""",

    "quantum_short.txt": """Quantum — Short notes
Key concepts: wavefunction psi, Schrödinger equation, quantization, operators.
Particle in a box: discrete energy levels E_n = (n^2 h^2)/(8 m L^2).
Importance of boundary conditions and normalization.
""",

    "ml_fundamentals.txt": """Machine Learning — Fundamentals
Supervised learning: regression, classification.
Common models: Linear Regression, Decision Trees, Random Forests.
Evaluation: accuracy, precision, recall, F1-score, ROC-AUC.
Cross-validation and hyperparameter tuning are essential for robust models.
""",

    "cv_anomaly_detection.txt": """Computer Vision — Anomaly Detection (notes)
Real-time anomaly detection may combine object detection (e.g., YOLO) with temporal models (LSTM).
Typical pipeline: frame capture -> detection -> tracking -> LSTM or statistical anomaly detection -> alert.
Edge deployment requires model quantization and low-latency inference.
""",

    "projects_summary.txt": """My Project Summaries (example)
1) Breast Cancer Classifier — Completed a pipeline with hyperparameter tuning and deployed using Joblib.
2) Smart Petrol Pump CV System — YOLO + LSTM based real-time anomaly detection and alerting.
3) Edge Anomaly Detection for Industrial Sensor Data — Synthetic data generation + edge inference.
4) House Price Prediction App — Flask + Docker + Gunicorn serving regression inference.
"""
}

for fname, text in docs.items():
    with open(os.path.join("data", fname), "w", encoding="utf-8") as f:
        f.write(text)

print("Wrote sample dataset into ./data/")
