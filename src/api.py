from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from src.model_service import predict


# -----------------------------
# Input Validation Schema
# -----------------------------
class PredictionRequest(BaseModel):
    latency: float
    error_rate: float
    cpu_usage: float
    memory_usage: float


app = FastAPI(
    title="Reliability Monitoring API",
    docs_url="/docs",
    redoc_url=None
)


# -----------------------------
# Health Endpoint
# -----------------------------
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "reliability-ml-api"
    }


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def home():
    return {"status": "ML Monitoring API Running"}


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def get_prediction(request: PredictionRequest):
    return predict(request.dict())
