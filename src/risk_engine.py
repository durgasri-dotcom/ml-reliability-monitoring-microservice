def compute_risk(df):

    df["risk_score"] = (
        df["error_rate"] * 0.5 +
        abs(df["latency_zscore"]) * 0.3 +
        abs(df["traffic_change"]) * 0.2
    )

    return df
