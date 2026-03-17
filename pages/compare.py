import streamlit as st
import pandas as pd

st.title("Compare Destinations")

data = pd.read_csv("data/destinations.csv")

place1 = st.selectbox("Destination 1",data["destination"])
place2 = st.selectbox("Destination 2",data["destination"])

st.subheader(place1)

st.write(data[data["destination"]==place1])

st.subheader(place2)

st.write(data[data["destination"]==place2])