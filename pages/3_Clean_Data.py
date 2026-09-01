import streamlit as st
import pandas as pd

st.title("🧹 3. Clean Data")

df = pd.read_csv("data/shipment_data.csv")

st.write(f"Starting with **{len(df)} rows** and **{df.shape[1]} columns**.")

st.subheader("Step 1: Drop Corrupted Columns")

st.write("""
`delivery_time_hours` and `expected_time_hours` were found to contain the
same value (`00:00.0`) in every single row — they carry no usable
information. Rather than filling or guessing values, the correct move is
to drop them and note why.
""")

broken_cols = ["delivery_time_hours", "expected_time_hours"]
st.code(f"df = df.drop(columns={broken_cols})")

df = df.drop(columns=broken_cols)
st.write("Columns after dropping:", list(df.columns))

st.subheader("Step 2: Fix the Non-Unique Identifier")

dupe_count_before = df["delivery_id"].duplicated().sum()
st.write(f"`delivery_id` had **{dupe_count_before}** duplicate values before "
         "cleaning, even though it's meant to be a unique key.")

st.write("""
Since we can't recover the *original* intended IDs, the cleaning
approach is to reset the identifier to a clean, guaranteed-unique
sequential ID, while keeping every original record.
""")

df = df.reset_index(drop=True)
df["delivery_id"] = df.index + 1
st.code('df["delivery_id"] = df.index + 1  # reassign a clean unique ID')

st.write("Duplicate `delivery_id` values after fix:",
         df["delivery_id"].duplicated().sum())

st.subheader("Step 2b: Flag a Suspected Capping Bug")

max_cost = df["delivery_cost"].max()
capped_count = (df["delivery_cost"] == max_cost).sum()
st.write(
    f"**{capped_count} shipments** share the exact same maximum cost value "
    f"(₹{max_cost:,.2f}), across otherwise different distances and weights. "
    "This strongly suggests the source data generation capped cost at an "
    "upper limit rather than these being genuinely identical shipments. "
    "The rows aren't dropped (their other fields are still usable), but "
    "this is flagged here as a known limitation of the dataset."
)

st.subheader("Step 3: Standard Checks (Duplicates & Missing Values)")

st.write("Fully duplicated rows:", df.duplicated().sum())
st.write("Missing values per column:")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.subheader("Step 4: Tidy Up Text Formatting")

st.write("""
Category columns are stored in lowercase in the raw file
(e.g. `xpressbees`, `west`). For display purposes we create title-cased
versions without losing the original values used for filtering.
""")

df["delivery_partner"] = df["delivery_partner"].str.strip().str.title()
df["delivery_partner"] = df["delivery_partner"].replace({
    "Dhl": "DHL",
    "Xpressbees": "XpressBees",
})
df["region"] = df["region"].str.strip().str.title()
df["weather_condition"] = df["weather_condition"].str.strip().str.title()
df["delivery_mode"] = df["delivery_mode"].str.strip().str.title()

st.subheader("Cleaned Data")
st.dataframe(df, use_container_width=True)

st.success("Cleaning completed!")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Cleaned Data",
    csv,
    "cleaned_shipment_data.csv",
    "text/csv"
)

st.info("""
### What did we do?

• Identified and dropped two columns that were entirely corrupted
  (`delivery_time_hours`, `expected_time_hours`)
• Detected that `delivery_id` was not actually unique, and reassigned a
  clean identifier
• Ran standard duplicate/missing-value checks (both came back clean)
• Standardized text formatting across category columns

This is a good example of why real-world cleaning has to go beyond
`isnull()` and `duplicated()` — the most damaging issues here weren't
missing values at all.
""")
