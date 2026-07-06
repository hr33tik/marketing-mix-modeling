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

def generate_channel_activity(df):
    """
    Generate weekly marketing activity for every channel
    at State-Week level.
    """

    # Create random number generator
    rng = np.random.default_rng(RANDOM_SEED)

    # Loop through every marketing channel
    for channel in CHANNELS:

        min_activity = CHANNEL_ACTIVITY[channel]["min"]
        max_activity = CHANNEL_ACTIVITY[channel]["max"]

        activity = []

        # Generate activity for every row
        for _, row in df.iterrows():

            state = row["State"]

            # State scaling factor
            multiplier = STATE_SCALE[state]

            value = rng.integers(
                min_activity,
                max_activity + 1
            )

            value = int(value * multiplier)

            activity.append(value)

        df[channel] = activity

    return df

def generate_calendar_features(df):
    """
    Generate calendar-based features for each State-Week.
    """

    df["Year"] = df["Week"].dt.year
    df["Month"] = df["Week"].dt.month
    df["Quarter"] = df["Week"].dt.quarter
    df["Week_Number"] = df["Week"].dt.isocalendar().week.astype(int)

    # Month End
    df["Month_End"] = (
        df["Week"] + pd.offsets.Week(1)
    ).dt.month != df["Week"].dt.month

    # Quarter End
    df["Quarter_End"] = (
        df["Week"] + pd.offsets.Week(1)
    ).dt.quarter != df["Week"].dt.quarter

    # Festival Flag
    df["Festival"] = df["Month"].isin(FESTIVAL_MONTHS).astype(int)

    # Holiday Flag
    # Placeholder for now.
    # We'll improve this later.
    df["Holiday"] = df["Festival"]

    return df

def geometric_adstock(series, decay):
    """
    Apply geometric adstock transformation.
    """

    adstock = np.zeros(len(series))

    adstock[0] = series.iloc[0]

    for i in range(1, len(series)):
        adstock[i] = (
            series.iloc[i]
            +
            decay * adstock[i - 1]
        )

    return adstock


def log_transformation(x):
    """
    Apply logarithmic transformation
    to model diminishing returns.
    """

    return np.log1p(x)

def generate_true_media_effects(df):
    """
    Apply the TRUE hidden media transformations
    (Adstock + Log).

    These variables are used ONLY for generating
    synthetic sales.

    They are NOT exported.
    """

    media_df = pd.DataFrame(index=df.index)

    media_df["State"] = df["State"]
    media_df["Week"] = df["Week"]

    for channel in CHANNELS:

        transformed_values = []

        decay = TRUE_ADSTOCK[channel]

        for state in STATES:

            state_df = (
                df[df["State"] == state]
                .sort_values("Week")
            )

            # Step 1 - Apply Adstock
            adstock = geometric_adstock(
                state_df[channel],
                decay
            )

            # Step 2 - Apply Log Transformation
            transformed = log_transformation(adstock)

            transformed_values.extend(transformed)

        media_df[channel] = transformed_values

    return media_df

def generate_sales(df, media_df):
    """
    Generate synthetic weekly units sold.

    Sales are generated using:
    - Base state demand
    - Carryover
    - Hidden transformed media
    - Seasonality
    - Random noise
    """

    rng = np.random.default_rng(RANDOM_SEED)

    sales = np.zeros(len(df))

    # Process one state at a time
    for state in STATES:

        state_idx = df[df["State"] == state].sort_values("Week").index

        previous_sales = 0

        for idx in state_idx:

            current_sales = BASE_STATE_DEMAND[state]

            # -----------------------------
            # Media Contribution
            # -----------------------------
            for channel in CHANNELS:

                current_sales += (
                    TRUE_COEFFICIENTS[channel]
                    *
                    media_df.loc[idx, channel]
                )

            # -----------------------------
            # Carryover
            # -----------------------------
            current_sales += (
                SALES_CARRYOVER
                *
                previous_sales
            )

            # -----------------------------
            # Seasonality
            # -----------------------------

            if df.loc[idx, "Month_End"]:
                current_sales *= (1 + MONTH_END_UPLIFT)

            if df.loc[idx, "Quarter_End"]:
                current_sales *= (1 + QUARTER_END_UPLIFT)

            if df.loc[idx, "Month"] == 12:
                current_sales *= (1 + YEAR_END_UPLIFT)

            # -----------------------------
            # Random Noise
            # -----------------------------
            current_sales += rng.normal(
                0,
                SALES_NOISE_STD
            )

            # Sales cannot be negative
            current_sales = max(0, current_sales)

            sales[idx] = current_sales

            previous_sales = current_sales

    df["Sales"] = sales.round().astype(int)

    return df

def generate_weekly_spends(df):
    """
    Generate weekly channel spend.

    Spend is calculated using
    total weekly activity across all states.
    """

    rng = np.random.default_rng(RANDOM_SEED)

    spend_rows = []

    weekly_activity = (
        df.groupby("Week")[CHANNELS]
        .sum()
        .reset_index()
    )

    for _, row in weekly_activity.iterrows():

        week = row["Week"]

        for channel in CHANNELS:

            activity = row[channel]

            base_spend = (
                activity
                *
                CHANNEL_COST[channel]
            )

            variation = rng.uniform(
                0.95,
                1.05
            )

            spend = base_spend * variation

            spend_rows.append({

                "Channel": channel,

                "Week": week,

                "Spend": round(spend, 2)

            })

    spend_df = pd.DataFrame(spend_rows)

    return spend_df