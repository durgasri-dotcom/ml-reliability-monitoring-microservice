from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.03, random_state=42)

def detect_anomalies(df):

    features = df[[
        "latency",
        "error_rate",
        "traffic"
    ]]

    df["anomaly"] = model.fit_predict(features)

    return df
