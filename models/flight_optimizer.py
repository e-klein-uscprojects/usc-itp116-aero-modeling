import pandas as pd
from sklearn.linear_model import LinearRegression

def optimize_flight(data):
    data = data.dropna()
    X = data[['wind_speed', 'air_traffic']]
    y = data['duration']

    model = LinearRegression()
    model.fit(X, y)

    data['optimized'] = model.predict(X)
    return data

