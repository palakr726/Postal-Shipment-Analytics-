# Project Report

## Postal & Shipment Data Wrangling using Python and Streamlit

### 1. Introduction

Data wrangling is the process of collecting, cleaning and preparing
data for analysis. This project applies that process to a real-world
last-mile delivery logistics dataset, and presents the results through
an interactive Streamlit application.

### 2. Objectives

- Load and inspect a large real-world shipment dataset.
- Identify data quality issues beyond simple missing-value checks.
- Clean and correct those issues.
- Check and correct class imbalance in delivery outcomes.
- Create visualizations of shipment patterns.
- Derive courier-, region- and weather-level insights.

### 3. Technologies Used

Python, Pandas, Matplotlib and Streamlit.

### 4. Dataset

25,000 shipment records across 9 courier partners (Delhivery, Blue
Dart, DHL, FedEx, Ekart, XpressBees, Shadowfax, Ecom Express, Amazon
Logistics), 5 regions, multiple package/vehicle types, and weather
conditions. Sourced from a public Kaggle dataset (see README for link).

### 5. Data Cleaning

Standard checks (`isnull()`, `duplicated()`) showed no missing values
and no duplicate rows. However, closer inspection revealed two
non-obvious issues:

1. `delivery_id`, intended as a unique identifier, contained thousands
   of duplicate values — corrected by reassigning a clean sequential ID.
2. `delivery_time_hours` and `expected_time_hours` contained an
   identical placeholder value in every row and carried no usable
   information — both columns were dropped.

Category columns were also standardized to title case for consistent
display.

### 6. Data Balancing

The `delayed` column (yes/no) is imbalanced: 18,331 on-time shipments
vs 6,669 delayed shipments. The minority class was balanced up to
match the majority class size using random oversampling with
replacement — the same technique demonstrated in the course example,
applied here to a real binary outcome.

### 7. Visualization

The project creates:

- Delivery status (delivered/delayed/failed) bar chart
- Package weight histogram
- Distance vs delivery cost scatter plot
- Package weight vs delivery cost scatter plot
- Delivery cost box plot, split by on-time vs delayed

### 8. Insights (Beyond the Base Template)

Using `groupby` aggregation, the project further answers:

- Which courier partner has the lowest delay rate?
- Does weather condition affect delay rate?
- Which region has the highest average shipping cost?
- Which delivery mode is most cost-efficient per kilometer?

### 9. Learning Outcomes

After completing this project:

- Applied Pandas methods for inspection, cleaning and aggregation on a
  real, non-trivial dataset.
- Learned to identify data quality issues that basic
  `isnull()`/`duplicated()` checks do not catch.
- Practiced class balancing via random oversampling.
- Built multiple chart types with Matplotlib.
- Built and structured a multi-page Streamlit application.
- Practiced translating raw data into business-relevant questions and
  answers.

### 10. Limitations & Future Work

- The dataset appears to have an upper cap on `delivery_cost` (250
  shipments share an identical maximum value) — likely an artifact of
  how the source data was generated, rather than a real-world price
  ceiling. This limits how far cost-driver analysis can be trusted at
  the high end.
- Random oversampling duplicates existing minority-class rows rather
  than generating new synthetic ones; a production pipeline would
  likely use a technique like SMOTE, and would balance only the
  training split after a train/test split, not the full dataset.
- The project is exploratory (EDA) rather than predictive — a natural
  next step would be training a classification model to predict
  `delayed` using the cleaned features, and evaluating it with
  precision/recall given the class imbalance.
- Cost and delay drivers are analyzed independently; a multivariate
  model (e.g. regression) would better separate the individual effect
  of distance, weight, mode, and weather on cost and delay together.

### 11. Conclusion

This project demonstrates an end-to-end data wrangling workflow on a
real-world logistics dataset — from identifying non-obvious data
quality problems, through cleaning and balancing, to visualization and
practical business insights.
