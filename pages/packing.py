import streamlit as st
import pandas as pd

st.title("Packing Assistant")

packing = pd.read_csv("data/packing.csv")

destination_type = st.selectbox(
    "Destination Type",
    packing["type"].unique()
)

items = packing[packing["type"]==destination_type]

st.subheader("Recommended Packing Items")

for item in items["item"]:
    st.write("•", item)