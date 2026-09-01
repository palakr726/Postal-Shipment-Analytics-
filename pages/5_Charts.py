import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import load_and_clean_data

st.title("📊 5. Data Visualization")

df = load_and_clean_data()

df["weight_bracket"] = pd.cut(
    df["package_weight_kg"],
    bins=[0, 15, 35, 50],
    labels=["Light (<15kg)", "Medium (15-35kg)", "Heavy (>35kg)"]
)

st.subheader("1. Delivery Status Breakdown")

status_count = df["delivery_status"].value_counts()

fig, ax = plt.subplots()
status_count.plot(kind="bar", ax=ax, color=["#2E7D32", "#F9A825", "#C62828"])
ax.set_xlabel("Delivery Status")
ax.set_ylabel("Number of Shipments")
ax.set_title("Delivered vs Delayed vs Failed")
st.pyplot(fig)

st.subheader("2. Package Weight Distribution")

fig, ax = plt.subplots()
ax.hist(df["package_weight_kg"], bins=20, color="#455A64")
ax.set_xlabel("Package Weight (kg)")
ax.set_ylabel("Number of Shipments")
ax.set_title("Package Weight Distribution")
st.pyplot(fig)

st.caption(
    "This is close to a uniform distribution — weight is spread evenly "
    "from ~0.7kg to ~50kg with no clustering. That's a real property of "
    "the data, not a plotting issue."
)

st.subheader("3. Distance vs Delivery Cost")

fig, ax = plt.subplots()
hb = ax.hexbin(df["distance_km"], df["delivery_cost"], gridsize=35, cmap="Blues", mincnt=1)
fig.colorbar(hb, ax=ax, label="Number of shipments")
ax.set_xlabel("Distance (km)")
ax.set_ylabel("Delivery Cost (INR)")
ax.set_title("Distance vs Delivery Cost (density)")
st.pyplot(fig)

corr_dist = df["distance_km"].corr(df["delivery_cost"])
st.caption(
    f"Correlation between distance and cost: **{corr_dist:.2f}** — a near-"
    "perfect relationship. Distance is overwhelmingly the main driver of "
    "delivery cost. A hexbin plot is used instead of a scatter plot here "
    "because a raw scatter of 25,000 overlapping points hides this "
    "pattern rather than showing it."
)

st.subheader("4. Delivery Cost by Package Weight Bracket")

fig, ax = plt.subplots()
data_by_weight = [
    df[df["weight_bracket"] == b]["delivery_cost"].dropna()
    for b in ["Light (<15kg)", "Medium (15-35kg)", "Heavy (>35kg)"]
]
bp = ax.boxplot(data_by_weight, tick_labels=["Light", "Medium", "Heavy"], patch_artist=True)
for patch, color in zip(bp["boxes"], ["#90CAF9", "#42A5F5", "#1565C0"]):
    patch.set_facecolor(color)
ax.set_xlabel("Package Weight Bracket")
ax.set_ylabel("Delivery Cost (INR)")
ax.set_title("Delivery Cost by Weight Bracket")
st.pyplot(fig)

corr_weight = df["package_weight_kg"].corr(df["delivery_cost"])
st.caption(
    f"Correlation between weight and cost: **{corr_weight:.2f}** — weak "
    "on its own, but grouping into brackets reveals a real, modest step "
    "up in cost as packages get heavier (median cost rises from roughly "
    "₹806 for light packages to ₹927 for heavy ones)."
)

st.subheader("5. Delivery Cost: On-Time vs Delayed")

on_time_cost = df[df["delayed"] == "no"]["delivery_cost"]
delayed_cost = df[df["delayed"] == "yes"]["delivery_cost"]

fig, ax = plt.subplots()
bp = ax.boxplot(
    [on_time_cost, delayed_cost],
    tick_labels=[f"On-Time (n={len(on_time_cost)})", f"Delayed (n={len(delayed_cost)})"],
    patch_artist=True,
    showmeans=True,
    meanprops={"marker": "D", "markerfacecolor": "white", "markeredgecolor": "black"}
)
bp["boxes"][0].set_facecolor("#66BB6A")
bp["boxes"][1].set_facecolor("#EF5350")

for i, series in enumerate([on_time_cost, delayed_cost], start=1):
    median_val = series.median()
    ax.annotate(
        f"median ₹{median_val:,.0f}",
        xy=(i, median_val),
        xytext=(i + 0.15, median_val),
        fontsize=9
    )

ax.set_ylabel("Delivery Cost (INR)")
ax.set_title("Delivery Cost: On-Time vs Delayed (◆ = mean)")
st.pyplot(fig)

st.caption(
    f"Delayed shipments cost noticeably more (median ₹{delayed_cost.median():,.0f} "
    f"vs ₹{on_time_cost.median():,.0f} on-time) — consistent with delays "
    "being more common on longer, costlier routes."
)

st.subheader("Simple Observations")

st.write("• Delivery outcomes are imbalanced — most shipments are delivered on time.")
st.write("• Package weight is roughly uniformly distributed across the dataset.")
st.write("• Distance is by far the strongest driver of delivery cost (r ≈ 0.99).")
st.write("• Weight has only a modest effect on cost, visible once grouped into brackets.")
st.write("• Delayed shipments tend to cost more than on-time ones.")

st.success("Now go to Page 6 for partner and region-level insights.")
