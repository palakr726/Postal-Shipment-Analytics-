import streamlit as st
import pandas as pd
from utils import load_and_clean_data

st.title("⚖️ 4. Balance Data")

df = load_and_clean_data()

st.subheader("Step 1: Check Delay Distribution")

st.write("""
The `delayed` column tells us whether each shipment was delayed
(`yes`/`no`). This is the target we'll balance, since it's the simplest
binary outcome in the dataset.
""")

delay_count = df["delayed"].value_counts()

st.write(delay_count)
st.bar_chart(delay_count)

st.write("""
One class has noticeably more records than the other — this dataset is
imbalanced.
""")

st.subheader("Step 2: Balance the Data")

on_time = df[df["delayed"] == "no"]
delayed = df[df["delayed"] == "yes"]

st.write("On-time deliveries:", len(on_time))
st.write("Delayed deliveries:", len(delayed))

if len(on_time) > len(delayed):
    small_group = delayed
    large_group = on_time
    small_name = "delayed"
else:
    small_group = on_time
    large_group = delayed
    small_name = "on-time"

if len(small_group) > 0:
    balanced_small_group = small_group.sample(
        len(large_group),
        replace=True,
        random_state=42
    )

    balanced_df = pd.concat(
        [large_group, balanced_small_group]
    )

    balanced_df = balanced_df.sample(
        frac=1,
        random_state=42
    ).reset_index(drop=True)

    st.subheader("After Balancing")

    st.write(balanced_df["delayed"].value_counts())
    st.bar_chart(balanced_df["delayed"].value_counts())

    st.dataframe(balanced_df.head(20), use_container_width=True)

    csv = balanced_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Balanced Data",
        csv,
        "balanced_shipment_data.csv",
        "text/csv"
    )

    st.success(
        f"The smaller class ({small_name}) was increased by randomly "
        "selecting records with replacement."
    )
else:
    st.error("The dataset does not contain both delayed and on-time records.")

st.info("""
### Simple idea behind balancing

Suppose we have:

On-time = 18,331 shipments
Delayed = 6,669 shipments

We randomly select delayed shipments again (with replacement) until we
have approximately:

On-time = 18,331 shipments
Delayed = 18,331 shipments

This is called **Random Oversampling**. Note: as with the course
example, this is a teaching demonstration — in a real ML pipeline,
balancing is normally applied to the training split only, after the
train/test split, to avoid leaking duplicated records into the test
set.
""")
