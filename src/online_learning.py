from sklearn.linear_model import SGDRegressor
import numpy as np

model = SGDRegressor()

initialized = False

def update_model(df):
    global initialized

    X = df[["latency","error_rate","traffic"]]
    y = df["latency"]

    if not initialized:
        model.partial_fit(X,y)
        initialized = True
    else:
        model.partial_fit(X,y)

    df["predicted_latency"] = model.predict(X)

    return df
