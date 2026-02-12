import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

NUM_SERVICES = 100

def generate_batch(batch_size=200):

    data = []

    now = datetime.now()

    for _ in range(batch_size):

        service_id = f"S{random.randint(1, NUM_SERVICES)}"

        latency = np.random.normal(200, 40)
        error_rate = abs(np.random.normal(0.02, 0.01))
        traffic = np.random.randint(1000, 50000)

        data.append([
            now,
            service_id,
            max(10, latency),
            error_rate,
            traffic
        ])

    return pd.DataFrame(
        data,
        columns=[
            "timestamp",
            "service_id",
            "latency",
            "error_rate",
            "traffic"
        ]
    )
