import streamlit as st
import pandas as pd

st.title("📍 Available Destinations")

try:
    data = pd.read_csv("data/destinations.csv")
    st.dataframe(data)

except Exception:
    st.error("Dataset format error. Please check destinations.csv.")