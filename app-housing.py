import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("housing.csv")

# Title
st.title("California Housing Data (1990) by Shihan Wang")

# Minimum median house value slider
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

# Filter by house value
df = df[df["median_house_value"] >= min_value]

# Subheader
st.subheader("See more filters in the sidebar:")

# Sidebar: Location type
location_types = df["ocean_proximity"].unique()

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types
)

# Filter by location type
df = df[df["ocean_proximity"].isin(selected_locations)]

# Sidebar: Income level
income_level = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

# Filter by income level
if income_level == "Low":
    df = df[df["median_income"] <= 2.5]

elif income_level == "Medium":
    df = df[
        (df["median_income"] > 2.5) &
        (df["median_income"] < 4.5)
    ]

else:
    df = df[df["median_income"] >= 4.5]

# Display map
st.map(df)

# Display histogram
fig, ax = plt.subplots()

ax.hist(
    df["median_house_value"],
    bins=30
)

ax.set_xlabel("Median House Value")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Median House Values")

st.pyplot(fig)