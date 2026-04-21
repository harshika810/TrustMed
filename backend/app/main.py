from fastapi import FastAPI
from app.routes import router
import jinja2

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    
    
    return {"message": "TrustMedX backend is running"}

@app.get("/moment")
def moment():
    return {"message": "This is a moment endpoint"}

@app.get("/activity")
def activity():
    return {"message": "This is an activity endpoint"}
@app.get("/systolic_bp")
def systolic_bp():
    return {"message": "This is a systolic blood pressure endpoint"}

@app.get("/diastolic_bp")
def diastolic_bp():
    return {"message": "This is a diastolic blood pressure endpoint"}

@app.get("/spo2")
def spo2():
    return {"message": "This is a SpO2 endpoint"}

@app.get("sleep_hours")
def sleep_hours():
    return {"message": "This is a sleep hours endpoint"}


