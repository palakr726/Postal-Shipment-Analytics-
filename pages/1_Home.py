import streamlit as st

st.title("🏠 1. Home")

st.header("Postal & Shipment Data Wrangling")

st.write("""
This project analyzes a real-world last-mile delivery logistics dataset
covering 25,000 shipments across multiple Indian courier partners. Data
wrangling means preparing raw data so it can be reliably used for
analysis — here, that includes discovering and fixing data quality
issues that a first glance at the dataset doesn't reveal.
""")

st.subheader("Project Objectives")

st.write("1. Load the dataset and inspect its structure.")
st.write("2. Identify data quality issues beyond simple missing values.")
st.write("3. Fix broken/unusable columns and non-unique identifiers.")
st.write("4. Understand class imbalance in delivery outcomes.")
st.write("5. Balance the data using random oversampling.")
st.write("6. Visualize shipment cost, weight and delay patterns.")
st.write("7. Derive partner-, region- and weather-level insights.")

st.subheader("Dataset Columns")

st.table({
    "Column": [
        "delivery_id", "delivery_partner", "package_type", "vehicle_type",
        "delivery_mode", "region", "weather_condition", "distance_km",
        "package_weight_kg", "delayed", "delivery_status",
        "delivery_rating", "delivery_cost"
    ],
    "Meaning": [
        "Shipment identifier (found to have duplicates — see Page 3)",
        "Courier company handling the shipment",
        "Category of goods shipped",
        "Vehicle used for delivery",
        "Service level: same day / express / two day / standard",
        "Delivery region: north / south / east / west / central",
        "Weather during delivery",
        "Distance covered, in kilometers",
        "Package weight, in kilograms",
        "Whether the delivery was delayed (yes/no)",
        "Final outcome: delivered / delayed / failed",
        "Customer rating (1-5)",
        "Total delivery cost, in INR"
    ]
})

st.info("""
**Note:** Two columns present in the raw file — `delivery_time_hours`
and `expected_time_hours` — were found to be entirely corrupted (every
row reads `00:00.0`) and are dropped during cleaning. See Page 3 for
details.
""")

st.success("Go to Page 2 to load and inspect the data.")
