# Configuration file for Marketing Mix Modeling Dataset Generator

# Project:
# Marketing Mix Modeling for FitFuel India

# Author:
# Hreetik Panda


from datetime import datetime


# ==========================================================
# RANDOM SEED
# ==========================================================

RANDOM_SEED = 42


# ==========================================================
# DATE CONFIGURATION
# ==========================================================

START_DATE = "2023-01-02"      # Monday
END_DATE = "2025-12-29"        # Monday

FREQUENCY = "W-MON"


# ==========================================================
# GEOGRAPHY
# ==========================================================

STATES = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]


# ==========================================================
# MARKETING CHANNELS
# ==========================================================

CHANNELS = [
    "Salesforce",
    "Email",
    "Website",
    "TV",
    "Meta",
    "Instagram",
    "Influencer"
]


# ==========================================================
# ACTIVITY RANGES
# (Weekly Activity)
# ==========================================================

CHANNEL_ACTIVITY = {

    "Salesforce": {
        "min": 300,
        "max": 2500
    },

    "Email": {
        "min": 2000,
        "max": 40000
    },

    "Website": {
        "min": 8000,
        "max": 120000
    },

    "TV": {
        "min": 80,
        "max": 500
    },

    "Meta": {
        "min": 100000,
        "max": 2500000
    },

    "Instagram": {
        "min": 80000,
        "max": 1800000
    },

    "Influencer": {
        "min": 2,
        "max": 30
    }

}


# ==========================================================
# STATE MULTIPLIERS
# Larger states naturally have more activity
# ==========================================================

STATE_SCALE = {

    "Maharashtra": 1.60,
    "Uttar Pradesh": 1.80,
    "Karnataka": 1.25,
    "Tamil Nadu": 1.30,
    "Gujarat": 1.25,
    "West Bengal": 1.20,
    "Telangana": 1.10,
    "Kerala": 0.90,
    "Punjab": 0.80,
    "Rajasthan": 1.10,
    "Madhya Pradesh": 1.20,
    "Bihar": 1.30,
    "Odisha": 0.90,
    "Assam": 0.75,
    "Jharkhand": 0.80,
    "Haryana": 0.85,
    "Chhattisgarh": 0.75,
    "Himachal Pradesh": 0.55,
    "Goa": 0.40,
    "Uttarakhand": 0.55,
    "Tripura": 0.35,
    "Meghalaya": 0.35,
    "Nagaland": 0.30,
    "Mizoram": 0.25,
    "Sikkim": 0.20,
    "Manipur": 0.35,
    "Arunachal Pradesh": 0.25,
    "Andhra Pradesh": 1.00
}


# ==========================================================
# BASE SALES
# Before marketing impact
# ==========================================================

BASE_SALES = {

    "min": 250,

    "max": 2500

}


# ==========================================================
# FESTIVAL MONTHS
# Used later while generating seasonality
# ==========================================================

FESTIVAL_MONTHS = [

    1,      # Republic Day

    8,      # Independence Day

    10,     # Dussehra

    11,     # Diwali

    12      # Christmas / New Year

]


# ==========================================================
# NOISE
# ==========================================================

NOISE_STD = 0.08

# ==========================================================
# SPENDS
# ==========================================================

SALESFORCE_COST_PER_CALL = 750

EMAIL_COST_PER_EMAIL = 0.85

META_CPM = 145

INSTAGRAM_CPM = 125

TV_COST_PER_GRP = 18000

INFLUENCER_COST_PER_POST = 60000


CHANNEL_COST = {
    "Salesforce": SALESFORCE_COST_PER_CALL,
    "Email": EMAIL_COST_PER_EMAIL,
    "Website": 0.25,              # Cost per website visit (INR)
    "TV": TV_COST_PER_GRP,
    "Meta": META_CPM / 1000,       # Convert CPM to Cost per Impression
    "Instagram": INSTAGRAM_CPM / 1000,
    "Influencer": INFLUENCER_COST_PER_POST
}


# ==========================================================
# OUTPUT FILES
# ==========================================================

RAW_DATA_FILE = "data/raw/raw_data.csv"

SPEND_DATA_FILE = "data/raw/weekly_spends.csv"

# ==========================================================
# TRUE ADSTOCK DECAYS
# (Used ONLY to generate synthetic sales)
# ==========================================================

TRUE_ADSTOCK = {

    "Salesforce": 0.65,
    "Email": 0.20,
    "Website": 0.10,
    "TV": 0.80,
    "Meta": 0.55,
    "Instagram": 0.45,
    "Influencer": 0.30

}


# ==========================================================
# TRUE COEFFICIENTS
# (Used ONLY while generating sales)
# ==========================================================

TRUE_COEFFICIENTS = {

    "Salesforce": 0.08,
    "Email": 0.002,
    "Website": 0.0008,
    "TV": 1.8,
    "Meta": 0.00005,
    "Instagram": 0.00004,
    "Influencer": 15

}


# ==========================================================
# SALES PARAMETERS
# ==========================================================

BASE_SALES = 300

SALES_CARRYOVER = 0.35

SALES_NOISE_STD = 30

# ==========================================================
# TRUE TRANSFORMATIONS
# ==========================================================

TRUE_TRANSFORMATIONS = {

    "Salesforce": "log",
    "Email": "log",
    "Website": "log",
    "TV": "log",
    "Meta": "log",
    "Instagram": "log",
    "Influencer": "log"

}

# ==========================================================
# BASE DEMAND
# ==========================================================

BASE_STATE_DEMAND = {
    state: int(500 * STATE_SCALE[state])
    for state in STATES
}


# ==========================================================
# SALES PARAMETERS
# ==========================================================

BASE_SALES = 300

SALES_CARRYOVER = 0.35

SALES_NOISE_STD = 25

AVERAGE_SELLING_PRICE = 2500


# ==========================================================
# SEASONALITY
# ==========================================================

MONTH_END_UPLIFT = 0.05

QUARTER_END_UPLIFT = 0.15

YEAR_END_UPLIFT = 0.10

