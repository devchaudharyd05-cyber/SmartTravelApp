import streamlit as st
import sys
import os
import pandas as pd

# allow imports from main project folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from iot_module import visited_locations

st.title("Travel History")

st.write("Here are the destinations recommended during this session.")

if visited_locations:

    # remove duplicates but keep order
    unique_places = list(dict.fromkeys(visited_locations))

    st.subheader("Visited Destinations")

    df = pd.DataFrame(unique_places, columns=["Destination"])

    st.dataframe(df, use_container_width=True)

    st.metric("Total Destinations Visited", len(unique_places))

    if st.button("Clear History"):
        visited_locations.clear()
        st.success("Travel history cleared")

else:
    st.info("No travel history yet. Get a recommendation first.")