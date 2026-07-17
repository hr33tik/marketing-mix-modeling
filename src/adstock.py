import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)

def geometric_adstock(series, decay):
    """
    Apply geometric adstock transformation.
    """

    result = np.zeros(len(series))

    result[0] = series.iloc[0]

    for i in range(1, len(series)):

        result[i] = (
            series.iloc[i]
            +
            decay * result[i - 1]
        )

    return result

def decay_grid():
    """
    Candidate decay values.
    """

    return np.arange(
        0,
        1.00,
        0.05
    )

def evaluate_single_channel(
    df,
    channel,
    decay
):
    """
    Evaluate one adstock decay for one channel.
    """

    temp = df.copy()

    temp[channel] = geometric_adstock(
        temp[channel],
        decay
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
        1
        -
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

        "Decay": decay,

        "R2": r2,

        "Adjusted_R2": adjusted_r2,

        "RMSE": rmse,

        "MAE": mae,

        "AIC": aic,

        "BIC": bic

    }

def find_best_decay(
    df,
    channel
):
    """
    Evaluate all candidate adstocks.
    """

    results = []

    for decay in decay_grid():

        metrics = evaluate_single_channel(
            df,
            channel,
            decay
        )

        results.append(metrics)

    results = pd.DataFrame(results)

    return results.sort_values(
        "R2",
        ascending=False
    )

