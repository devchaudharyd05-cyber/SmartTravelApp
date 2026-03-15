import streamlit as st
from auth import authenticate

st.set_page_config(
    page_title="Smart Travel App",
    page_icon="✈️",
    layout="wide"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("🌍 Smart Travel Recommendation System")
    st.subheader("Login to continue")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if authenticate(username, password):

            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()

        else:
            st.error("Invalid username or password")


# DASHBOARD AFTER LOGIN
else:

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Home", "Destinations", "Recommendation", "Add Destination"]
    )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    if page == "Home":
        st.switch_page("pages/home.py")

    elif page == "Destinations":
        st.switch_page("pages/destinations.py")

    elif page == "Recommendation":
        st.switch_page("pages/recommendation.py")

    elif page == "Add Destination":
        st.switch_page("pages/add_destination.py")