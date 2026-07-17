import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)

def linear_transform(series):
    return series

def log_transform(series):
    return np.log1p(series)

def root_transform(series):
    return np.sqrt(series)

def power_transform(series):
    return np.power(series, 0.5)

def negative_exponential(series):
    """
    Negative exponential transformation.
    """

    max_value = series.max()

    if max_value == 0:
        return series

    return 1 - np.exp(-series / max_value)

def negative_exponential(series):
    """
    Negative exponential transformation.
    """

    max_value = series.max()

    if max_value == 0:
        return series

    return 1 - np.exp(-series / max_value)

TRANSFORMATIONS = {

    "Linear": linear_transform,

    "Log": log_transform,

    "Root": root_transform,

    "Power": power_transform,

    "Negative_Exponential": negative_exponential

}

def evaluate_transformation(
    df,
    channel,
    transformation_name
):
    """
    Evaluate one transformation.
    """

    temp = df.copy()

    transform = TRANSFORMATIONS[
        transformation_name
    ]

    temp[channel] = transform(
        temp[channel]
    )

    X = temp[[channel]]

    y = temp["Sales"]

    model = LinearRegression()

    model.fit(X, y)

    prediction = model.predict(X)

    n = len(y)

    p = 1

    r2 = r2_score(
        y,
        prediction
    )

    adjusted_r2 = (
        1 -
        (1-r2)*(n-1)/(n-p-1)
    )

    rmse = np.sqrt(
        mean_squared_error(
            y,
            prediction
        )
    )

    mae = mean_absolute_error(
        y,
        prediction
    )

    rss = np.sum(
        (y-prediction)**2
    )

    aic = (
        n*np.log(rss/n)
        +
        2*(p+1)
    )

    bic = (
        n*np.log(rss/n)
        +
        np.log(n)*(p+1)
    )

    return {

        "Transformation": transformation_name,

        "R2": r2,

        "Adjusted_R2": adjusted_r2,

        "RMSE": rmse,

        "MAE": mae,

        "AIC": aic,

        "BIC": bic

    }

def find_best_transformation(
    df,
    channel
):

    results = []

    for transformation in TRANSFORMATIONS.keys():

        metrics = evaluate_transformation(
            df,
            channel,
            transformation
        )

        results.append(metrics)

    results = pd.DataFrame(results)

    return results.sort_values(
        "R2",
        ascending=False
    )

