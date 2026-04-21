from fastapi import FastAPI
from app.routes import router
import jinja2

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    
    
    return {"message": "TrustMedX backend is running"}

