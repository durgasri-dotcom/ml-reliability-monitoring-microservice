import pandas as pd
import numpy as np

def predict(data: dict):
    """
    Simulated ML prediction engine
    """

    latency = data.get("latency", 0)
    error_rate = data.get("error_rate", 0)

    risk_score = (latency * 0.6) + (error_rate * 400)

    if risk_score > 300:
        level = "HIGH"
    elif risk_score > 150:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": level
    }
