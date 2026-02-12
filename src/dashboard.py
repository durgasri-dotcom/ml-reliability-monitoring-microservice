import streamlit as st
import time
from monitoring_pipeline import run_pipeline
from metrics_engine import compute_system_health
from config import REFRESH_INTERVAL

st.set_page_config(layout="wide")

st.title("Enterprise ML Reliability Monitoring System")

placeholder = st.empty()

while True:

    df = run_pipeline()

    health = compute_system_health(df)

    with placeholder.container():

        c1,c2,c3,c4 = st.columns(4)

        c1.metric("Avg Latency", round(health["avg_latency"],2))
        c2.metric("Error Rate", round(health["error_rate"],4))
        c3.metric("Anomalies", health["anomaly_count"])
        c4.metric("High Risk Services", health["high_risk"])

        st.subheader("High Risk Services")

        st.dataframe(
            df.sort_values("risk_score",ascending=False)
            .head(15)
        )

        st.subheader("Alerts")

        st.dataframe(
            df[df["alert"]==True][[
                "service_id",
                "risk_score",
                "explanation"
            ]]
        )

    time.sleep(REFRESH_INTERVAL)
