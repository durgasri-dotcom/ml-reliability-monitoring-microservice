from config import ALERT_THRESHOLD

def generate_alerts(df):

    df["alert"] = df["risk_score"] > ALERT_THRESHOLD

    return df
