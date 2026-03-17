import streamlit as st

st.title("Trip Cost Calculator")

travel = st.number_input("Travel Cost")
hotel = st.number_input("Hotel Cost")
food = st.number_input("Food Cost")
activities = st.number_input("Activities Cost")

total = travel + hotel + food + activities

st.subheader("Estimated Total Trip Cost")

st.write("₹", total)