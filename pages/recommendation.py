import streamlit as st
import pandas as pd
import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ml_model import recommend_destination
from iot_module import log_location

st.title("AI Travel Recommendation")

# Load destination data
data = pd.read_csv("data/destinations.csv")

# User inputs
budget = st.slider("Select Your Budget (₹)", 2000, 100000, 20000)

likes_beach = st.selectbox(
    "Do you like beach destinations?",
    [1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# Recommendation button
if st.button("Recommend Destination"):

    place = recommend_destination(likes_beach, budget)

    st.success(f"Recommended Destination: **{place}**")

    # Save travel history
    log_location(place)

    # Get destination info
    result = data[data["destination"] == place]

    if not result.empty:

        info = result.iloc[0]

        st.subheader("Destination Details")

        col1, col2 = st.columns(2)

        col1.write("**Type:**", info["type"])
        col1.write("**Weather:**", info["weather"])
        col1.write("**Temperature:**", info["temperature"], "°C")

        col2.write("**Travel Price:** ₹", info["travel_price"])
        col2.write("**Rating:** ⭐", info["rating"])
        col2.write("**Best Time to Visit:**", info["best_time"])

    else:
        st.error("Destination details not found.")