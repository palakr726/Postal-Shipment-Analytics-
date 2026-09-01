"""
Shared data loading and cleaning logic, used by every page so the
cleaning steps are written once instead of being copy-pasted.
"""

import pandas as pd
import streamlit as st


@st.cache_data
def load_and_clean_data(path: str = "data/shipment_data.csv") -> pd.DataFrame:
    """
    Loads the raw shipment CSV and applies the cleaning steps explained
    on Page 3: drops corrupted columns, reassigns a clean unique ID,
    and standardizes text casing.
    """
    df = pd.read_csv(path)

    df = df.drop(columns=["delivery_time_hours", "expected_time_hours"])
    df = df.reset_index(drop=True)
    df["delivery_id"] = df.index + 1

    for col in ["delivery_partner", "region", "weather_condition", "delivery_mode"]:
        df[col] = df[col].str.strip().str.title()
    df["delivery_partner"] = df["delivery_partner"].replace({
        "Dhl": "DHL",
        "Xpressbees": "XpressBees",
    })

    return df
