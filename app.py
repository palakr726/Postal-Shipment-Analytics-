import streamlit as st

st.set_page_config(page_title="Postal & Shipment Analytics", page_icon="📦")

st.title("📦 Postal & Shipment Data Wrangling")
st.write(
    "A data wrangling project analyzing 25,000 real-world last-mile "
    "delivery records across Indian courier partners — built with "
    "Python, Pandas and Streamlit."
)

st.subheader("What will we learn?")
st.write("""
This project walks through a full data wrangling workflow:

1. Load shipment data
2. Understand and inspect the data
3. Clean the data — including issues that go beyond missing values
4. Balance the delivery outcome classes
5. Visualize shipment patterns
6. Derive courier-, region- and weather-level insights
""")

st.info("Use the pages in the left sidebar to go through the project step by step.")

st.subheader("Tools Used")
st.write("• Python")
st.write("• Pandas")
st.write("• Matplotlib")
st.write("• Streamlit")

st.subheader("Project Dataset")
st.write("""
25,000 shipment records sourced from a public delivery logistics dataset
on Kaggle, covering 9 courier partners, 5 regions, multiple package and
vehicle types, weather conditions, and delivery outcomes.
""")

st.caption(
    "Dataset source: Delivery Logistics Dataset (India – Multi-Partner), "
    "Kaggle. Used for educational purposes."
)
