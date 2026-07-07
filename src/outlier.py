import pandas as pd
import numpy as np


def calculate_iqr_bounds(series):
    """
    Calculate lower and upper bounds using IQR.
    """

    q1 = series.quantile(0.25)

    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr

    upper = q3 + 1.5 * iqr

    return lower, upper

def identify_outliers(series):
    """
    Return boolean mask of outliers.
    """

    lower, upper = calculate_iqr_bounds(series)

    return (
        (series < lower)
        |
        (series > upper)
    )

def winsorize_series(series):
    """
    Cap outliers using IQR bounds.
    """

    lower, upper = calculate_iqr_bounds(series)

    return series.clip(
        lower,
        upper
    )