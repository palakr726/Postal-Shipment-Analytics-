# Postal & Shipment Data Wrangling

A data wrangling and exploratory analysis project on a real-world
last-mile delivery logistics dataset, built with Python, Pandas and
Streamlit.

**Live app:** _add your Streamlit Cloud link here once deployed_

## Key Findings

- **250 shipments share a non-unique `delivery_id`**, and **2 of the
  13 raw columns are entirely corrupted** — found only by looking past
  a standard `isnull()`/`duplicated()` check.
- **Distance explains delivery cost almost entirely** (r ≈ 0.99);
  package weight has only a modest effect once grouped into brackets.
- **250 shipments share an identical maximum cost value**, suggesting
  a capping artifact in the source data (see Limitations in the report).
- Delayed shipments have a noticeably higher median cost (₹1,075 vs
  ₹792 on-time).

## Overview

This project takes a 25,000-row real-world shipment dataset spanning
9 Indian courier partners and walks through a full data wrangling
pipeline: inspection, cleaning, class balancing, and visualization —
plus a bonus insights page answering practical logistics questions
(which courier partner has the best on-time record, does weather
actually affect delays, which region is costliest to ship to, etc.).

## What makes this more than a cleaning exercise

A first pass at this dataset shows **zero missing values and zero
duplicate rows** — but that doesn't mean it's clean:

- `delivery_id`, meant to be a unique key, was found to repeat for
  hundreds of rows.
- `delivery_time_hours` and `expected_time_hours` turned out to be
  entirely corrupted — every row contained the same placeholder value.

Identifying and handling these issues (rather than relying only on
`isnull()`/`duplicated()`) is the core wrangling work in this project.
See `pages/3_Clean_Data.py` for the full walkthrough.

## Pages

| Page | What it covers |
|---|---|
| 1. Home | Project overview and dataset description |
| 2. Load Data | Shape, dtypes, missing values, identifier uniqueness check |
| 3. Clean Data | Drops corrupted columns, fixes non-unique IDs, standardizes text |
| 4. Balance Data | Checks and fixes class imbalance in delivery outcomes via random oversampling |
| 5. Charts | Delivery status breakdown, weight distribution, cost relationships |
| 6. Insights | Partner/region/weather-level analysis using `groupby` |

## Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit

## Running Locally

```bash
git clone <your-repo-url>
cd postal-shipment-analytics
pip install -r requirements.txt
streamlit run app.py
```

## Dataset

Source: [Delivery Logistics Dataset (India – Multi-Partner)](https://www.kaggle.com/datasets/kundanbedmutha/delivery-logistics-dataset-india-multi-partner)
on Kaggle. Used here for educational purposes.

## Author

Palak — BSc Data Science & Business Analytics, HSNC University, Mumbai.
