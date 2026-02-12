import pandas as pd

def create_features(df):

    df["latency_zscore"] = (
        df["latency"] - df["latency"].mean()
    ) / df["latency"].std()

    df["error_spike"] = df["error_rate"] > df["error_rate"].mean() * 1.5

    df["traffic_change"] = df["traffic"].pct_change().fillna(0)

    return df
