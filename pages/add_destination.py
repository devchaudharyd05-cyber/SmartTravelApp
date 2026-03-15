import streamlit as st
import pandas as pd

st.title("➕ Add Destination")

# Input fields
place = st.text_input("Destination Name")

likes_beach = st.selectbox(
    "Is it a beach destination?",
    [1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

budget = st.number_input("Recommended Budget", min_value=1000)

price = st.number_input("Estimated Travel Price", min_value=1000)

rating = st.slider("Rating", 1.0, 5.0)

# Add button
if st.button("Add Destination"):

    if place.strip() == "":
        st.warning("Please enter a destination name")

    else:

        # Create new row
        new_row = pd.DataFrame([{
            "destination": place,
            "likes_beach": likes_beach,
            "budget": budget,
            "price": price,
            "rating": rating
        }])

        # Load existing dataset
        try:
            data = pd.read_csv("data/destinations.csv")
        except:
            data = pd.DataFrame(columns=[
                "destination",
                "likes_beach",
                "budget",
                "price",
                "rating"
            ])

        # Append new row
        data = pd.concat([data, new_row], ignore_index=True)

        # Save file safely
        data.to_csv("data/destinations.csv", index=False)

        st.success("Destination added successfully!")

        st.rerun()