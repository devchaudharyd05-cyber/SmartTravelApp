import streamlit as st
import pandas as pd

st.title("➕ Add Destination")

place = st.text_input("Destination Name")

likes_beach = st.selectbox(
    "Beach destination?",
    [1,0],
    format_func=lambda x: "Yes" if x==1 else "No"
)

budget = st.number_input("Budget")

price = st.number_input("Price")

rating = st.slider("Rating",1.0,5.0)

if st.button("Add Destination"):

    if place == "":
        st.warning("Please enter destination name")

    else:

        new_data = pd.DataFrame(
            [[place,likes_beach,budget,price,rating]],
            columns=["destination","likes_beach","budget","price","rating"]
        )

        new_data.to_csv(
            "data/destinations.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("Destination added successfully!")