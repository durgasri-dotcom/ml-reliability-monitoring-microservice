def compute_system_health(df):

    health = {}

    health["avg_latency"] = df["latency"].mean()
    health["error_rate"] = df["error_rate"].mean()
    health["anomaly_count"] = int((df["anomaly"]==-1).sum())
    health["high_risk"] = int((df["risk_score"]>0.75).sum())

    return health
