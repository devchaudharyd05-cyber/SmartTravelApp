import streamlit as st
import pandas as pd

st.title("➕ Add Destination")

place = st.text_input("Destination Name")

likes_beach = st.selectbox(
    "Beach destination?",
    [1,0],
    format_func=lambda x: "Yes" if x==1 else "No"
)

budget = st.number_input("Budget", min_value=1000)

price = st.number_input("Price", min_value=1000)

rating = st.slider("Rating",1.0,5.0)

if st.button("Add Destination"):

    if place.strip() == "":
        st.warning("Please enter destination name")

    else:

        new_row = {
            "destination": place,
            "likes_beach": likes_beach,
            "budget": budget,
            "price": price,
            "rating": rating
        }

        df = pd.DataFrame([new_row])

        df.to_csv(
            "data/destinations.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("Destination added successfully!")