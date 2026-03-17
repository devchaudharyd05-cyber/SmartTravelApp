import streamlit as st
import pandas as pd

st.title("Explore Destinations")

data = pd.read_csv("data/destinations.csv")

# Search
search = st.text_input("Search destination")

if search:
    data = data[data["destination"].str.contains(search, case=False)]

# Budget filter
budget = st.slider("Max Travel Price",2000,100000,20000)

data = data[data["travel_price"] <= budget]

# Weather filter
weather = st.selectbox(
    "Preferred Weather",
    ["All","Cold","Hot","Moderate","Tropical"]
)

if weather != "All":
    data = data[data["weather"].str.contains(weather)]

st.dataframe(data)