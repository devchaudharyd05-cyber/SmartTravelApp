import streamlit as st
import pandas as pd

st.title("Smart Travel Dashboard")

data = pd.read_csv("data/destinations.csv")

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Destinations", len(data))
col2.metric("Average Rating", round(data["rating"].mean(), 2))
col3.metric("Average Travel Price", round(data["travel_price"].mean(), 2))

st.subheader("Top Rated Destinations")

# Sort by rating
top = data.sort_values(by="rating", ascending=False)

# Show only important columns
top_display = top[[
    "destination",
    "type",
    "travel_price",
    "rating",
    "weather",
    "best_time"
]]

st.dataframe(top_display, use_container_width=True)