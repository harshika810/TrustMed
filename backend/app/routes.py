from fastapi import APIRouter
from app.models import HealthData
from app.db import health_collection

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