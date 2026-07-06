import numpy as np
import pandas as pd
import os

from config import *


def generate_weeks():
    """
    Generate weekly dates.
    """

    weeks = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq=FREQUENCY
    )

    return weeks


def generate_state_week_grid():
    """
    Create all State × Week combinations.
    """

    weeks = generate_weeks()

    df = pd.MultiIndex.from_product(
        [STATES, weeks],
        names=["State", "Week"]
    ).to_frame(index=False)

    return df