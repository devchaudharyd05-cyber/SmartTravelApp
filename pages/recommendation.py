import streamlit as st
from ml_model import recommend_destination

st.title("🤖 Travel Recommendation")

likes_beach = st.selectbox(
    "Do you like beaches?",
    [1,0],
    format_func=lambda x: "Yes" if x==1 else "No"
)

budget = st.number_input("Enter your travel budget")

if st.button("Recommend"):

    result = recommend_destination(likes_beach,budget)

    st.success(f"Recommended Destination: {result}")