import numpy as np

def detect_drift(df):

    drift_score = abs(df["latency"].mean() - 200)

    df["drift_flag"] = drift_score > 20

    return df
