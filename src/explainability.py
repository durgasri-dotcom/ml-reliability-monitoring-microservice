def explain_anomalies(df):

    explanations = []

    for _,row in df.iterrows():

        reason = []

        if row["latency_zscore"] > 2:
            reason.append("High latency spike")

        if row["error_rate"] > 0.05:
            reason.append("Elevated error rate")

        if abs(row["traffic_change"]) > 0.5:
            reason.append("Traffic surge")

        explanations.append(", ".join(reason) if reason else "Normal")

    df["explanation"] = explanations

    return df
