import streamlit as st
import pandas as pd

st.title("📍 Available Destinations")

data = pd.read_csv("data/destinations.csv")

st.dataframe(data)