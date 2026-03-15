import streamlit as st
import pandas as pd

st.title("📍 Available Destinations")

try:

    data = pd.read_csv("data/destinations.csv", on_bad_lines="skip")

    if data.empty:
        st.warning("No destinations available")

    else:
        st.dataframe(data)

except Exception as e:

    st.error("Error loading destinations dataset")

# Refresh button
if st.button("Refresh Destinations"):
    st.rerun()