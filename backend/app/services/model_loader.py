import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join("backend", "ml", "ml", "data", "risk_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_risk(sleep_hours, heart_rate, activity, systolic_bp, diastolic_bp, spo2):
    input_data = pd.DataFrame([{
        "sleep_hours": sleep_hours,
        "heart_rate": heart_rate,
        "activity": activity,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp
    }])

    ml_prediction = model.predict(input_data)[0]

    if spo2 < 92:
        return "High Risk (Low Oxygen)"
    elif systolic_bp > 140 or diastolic_bp > 90:
        return "High Risk (High BP)"
    elif ml_prediction == 1:
        return "Moderate Risk"
    else:
        return "Low Risk"