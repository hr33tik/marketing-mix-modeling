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

# ==========================================================
# OUTPUT FILES
# ==========================================================

RAW_DATA_FILE = "data/raw/raw_data.csv"

SPEND_DATA_FILE = "data/raw/weekly_spends.csv"