import numpy as np

def predict_incident(df):

    df["incident_probability"] = (
        df["error_rate"] * 0.6 +
        abs(df["latency_zscore"]) * 0.3 +
        (df["traffic"] / df["traffic"].max()) * 0.1
    )

    df["incident_risk"] = df["incident_probability"] > 0.65

    return df
