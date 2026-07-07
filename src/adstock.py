import numpy as np


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

def generate_decay_grid():
    """
    Candidate decay values.
    """

    return np.arange(
        0,
        1.00,
        0.05
    )