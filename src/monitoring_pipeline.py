from data_generator import generate_batch
from feature_engineering import create_features
from anomaly_engine import detect_anomalies
from drift_detection import detect_drift
from risk_engine import compute_risk
from online_learning import update_model
from incident_predictor import predict_incident
from explainability import explain_anomalies
from alert_engine import generate_alerts

def run_pipeline():

    df = generate_batch()

    df = create_features(df)

    df = update_model(df)

    df = detect_anomalies(df)

    df = detect_drift(df)

    df = compute_risk(df)

    df = predict_incident(df)

    df = explain_anomalies(df)

    df = generate_alerts(df)

    return df

