from fastapi import APIRouter
from app.models import HealthData
from app.db import health_collection
from blockchain.blockchain_service import generate_hash

router = APIRouter()

@router.post("/predict")
def predict(data: HealthData):
    risk_score = 0.82
    risk_level = "High"

    report = {
        "user_id": "U001",
        "risk_score": risk_score,
        "risk_level": risk_level,
        "model_version": "v1.0"
    }

    report_hash = generate_hash(report)

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "report_hash": report_hash
    }

@router.post("/verify")
def verify(report: dict, stored_hash: str):
    new_hash = generate_hash(report)

    if new_hash == stored_hash:
        return {"status": "Verified"}
    else:
        return {"status": "Tampered"}