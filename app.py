import streamlit as st
from auth import authenticate

st.set_page_config(
    page_title="Smart Travel App",
    page_icon="✈️",
    layout="wide"
)

st.title("🌍 Smart Travel Recommendation System")

st.write("Login to explore travel destinations.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if authenticate(username,password):

        st.success("Login successful!")
        st.write("Use the sidebar to navigate through the app.")

    else:

        st.error("Invalid username or password")