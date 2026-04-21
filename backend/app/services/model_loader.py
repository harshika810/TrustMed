from fastapi import APIRouter
from app.models import HealthData
from app.db import health_collection

# ✅ ML import
from app.services.model_loader import predict_risk

# ✅ Blockchain hash
from blockchain.blockchain_service import generate_hash

router = APIRouter()


@router.get("/test")
def test_api():
    return {"status": "API working fine"}


@router.get("/test-db")
def test_db():
    health_collection.insert_one({"msg": "mongo working"})
    return {"status": "MongoDB connected"}


@router.post("/upload-health-data")
def upload_health_data(data: HealthData):
    health_collection.insert_one(data.dict())
    return {
        "message": "Health data saved successfully",
        "data": data
    }


# 🔥 FINAL PREDICT ROUTE (ML + Blockchain)
@router.post("/predict")
def predict(data: HealthData):

    # ✅ ML prediction
    risk_score, risk_level = predict_risk(
        data.sleep_hours,
        data.heart_rate,
        data.activity,
        data.systolic_bp,
        data.diastolic_bp,
        data.spo2
    )

    # ✅ Report
    report = {
        "user_id": "U001",
        "risk_score": risk_score,
        "risk_level": risk_level,
        "model_version": "v1.0"
    }

    # ✅ Hash generate
    report_hash = generate_hash(report)

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "report_hash": report_hash
    }


# 🔥 VERIFY ROUTE
@router.post("/verify")
def verify(data: dict):
    report = data["report"]
    stored_hash = data["stored_hash"]

    new_hash = generate_hash(report)

    if new_hash == stored_hash:
        return {"status": "Verified"}
    else:
        return {"status": "Tampered"}