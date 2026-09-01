import streamlit as st
import pandas as pd

st.title("📂 2. Load and Understand Data")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/shipment_data.csv")
    st.info("Using the sample shipment_data.csv file.")

st.subheader("First 10 Records")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Number of Rows and Columns")

col1, col2 = st.columns(2)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

st.subheader("Column Names")
st.write(list(df.columns))

st.subheader("Data Types")
st.write(df.dtypes)

st.subheader("Missing Values")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))
st.caption(
    "No missing values here — but that doesn't mean the data is clean. "
    "See Page 3 for issues a `.isnull()` check alone won't catch."
)

st.subheader("Basic Statistics")
st.dataframe(df.describe(), use_container_width=True)

st.subheader("Row-Level Duplicate Check")
st.write("Fully duplicated rows:", df.duplicated().sum())

st.subheader("Identifier Uniqueness Check")
if "delivery_id" in df.columns:
    id_dupes = df["delivery_id"].duplicated().sum()
    st.write("Duplicate `delivery_id` values:", id_dupes)
    if id_dupes > 0:
        st.warning(
            "`delivery_id` is supposed to uniquely identify each shipment, "
            "but it doesn't. This is a data quality issue a standard "
            "`duplicated()` row-check misses, since the full rows differ."
        )
else:
    st.caption("No `delivery_id` column found in this file — skipping identifier check.")

st.success("Now go to Page 3 to clean the data.")
