from pydantic import BaseModel
from datetime import datetime

class HealthData(BaseModel):
    user_id: str
    timestamp: datetime
    heart_rate: int
    spo2: int
    activity_level: str
    sleep_hours: float
    wake_interruptions: int