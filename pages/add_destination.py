import streamlit as st
import pandas as pd

st.title("Add New Destination")

destination = st.text_input("Destination Name")

type = st.selectbox(
    "Destination Type",
    ["Beach","Mountain","City","Hill Station"]
)

likes_beach = st.selectbox("Beach Preference",[1,0])

budget = st.number_input("Recommended Budget")

travel_price = st.number_input("Travel Price")

rating = st.slider("Rating",1.0,5.0,4.0)

weather = st.text_input("Weather Type")

temperature = st.number_input("Average Temperature")

best_time = st.text_input("Best Time To Visit")


if st.button("Add Destination"):

    new_data = pd.DataFrame([{
        "destination":destination,
        "type":type,
        "likes_beach":likes_beach,
        "budget":budget,
        "travel_price":travel_price,
        "rating":rating,
        "weather":weather,
        "temperature":temperature,
        "best_time":best_time
    }])

    data = pd.read_csv("data/destinations.csv")

    data = pd.concat([data,new_data],ignore_index=True)

    data.to_csv("data/destinations.csv",index=False)

    st.success("Destination Added Successfully")