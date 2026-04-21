from pydantic import BaseModel


class RiskInput(BaseModel):
    sleep_hours: float
    heart_rate: float
    activity: float
    systolic_bp: float
    diastolic_bp: float
    spo2: float