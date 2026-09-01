import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_and_clean_data

st.title("🔎 6. Insights")

st.write("""
This page goes beyond the standard load → clean → balance → chart
template to answer a few practical business questions using `groupby`
— the kind of analysis a logistics team would actually want.
""")

df = load_and_clean_data()
df["is_delayed"] = (df["delayed"] == "yes").astype(int)

st.subheader("1. Which courier partner has the best on-time record?")

partner_stats = df.groupby("delivery_partner").agg(
    Shipments=("delivery_id", "count"),
    Avg_Cost=("delivery_cost", "mean"),
    Avg_Rating=("delivery_rating", "mean"),
    Delay_Rate_Pct=("is_delayed", "mean"),
)
partner_stats["Delay_Rate_Pct"] = (partner_stats["Delay_Rate_Pct"] * 100).round(1)
partner_stats["Avg_Cost"] = partner_stats["Avg_Cost"].round(0)
partner_stats["Avg_Rating"] = partner_stats["Avg_Rating"].round(2)
partner_stats = partner_stats.sort_values("Delay_Rate_Pct")

st.dataframe(partner_stats, use_container_width=True)

fig, ax = plt.subplots()
partner_stats["Delay_Rate_Pct"].sort_values().plot(kind="barh", ax=ax, color="#1565C0")
ax.set_xlabel("Delay Rate (%)")
ax.set_title("Delay Rate by Courier Partner")
st.pyplot(fig)

st.subheader("2. Does weather actually affect delays?")

weather_stats = df.groupby("weather_condition").agg(
    Shipments=("delivery_id", "count"),
    Delay_Rate_Pct=("is_delayed", "mean"),
)
weather_stats["Delay_Rate_Pct"] = (weather_stats["Delay_Rate_Pct"] * 100).round(1)
weather_stats = weather_stats.sort_values("Delay_Rate_Pct", ascending=False)

st.dataframe(weather_stats, use_container_width=True)

fig, ax = plt.subplots()
weather_stats["Delay_Rate_Pct"].plot(kind="bar", ax=ax, color="#EF6C00")
ax.set_ylabel("Delay Rate (%)")
ax.set_title("Delay Rate by Weather Condition")
st.pyplot(fig)

st.subheader("3. Which region is costliest to ship to, on average?")

region_stats = df.groupby("region").agg(
    Shipments=("delivery_id", "count"),
    Avg_Cost=("delivery_cost", "mean"),
    Avg_Distance=("distance_km", "mean"),
).round(1)
region_stats = region_stats.sort_values("Avg_Cost", ascending=False)

st.dataframe(region_stats, use_container_width=True)

st.subheader("4. Does delivery mode affect cost per kilometer?")

df["cost_per_km"] = df["delivery_cost"] / df["distance_km"].replace(0, pd.NA)

mode_stats = df.groupby("delivery_mode")["cost_per_km"].mean().round(2).sort_values(ascending=False)
st.dataframe(mode_stats.to_frame("Avg Cost per KM"), use_container_width=True)

fig, ax = plt.subplots()
mode_stats.plot(kind="bar", ax=ax, color="#6A1B9A")
ax.set_ylabel("Avg Cost per KM (INR)")
ax.set_title("Cost Efficiency by Delivery Mode")
st.pyplot(fig)

st.success("""
These four questions demonstrate `groupby`, multi-column aggregation,
and deriving new features (`is_delayed`, `cost_per_km`) — going one
step past the basic cleaning/charting workflow.
""")
