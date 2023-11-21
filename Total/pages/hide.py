import streamlit as st

# Use a checkbox to determine whether to show the element
show_element = st.checkbox("Show Element")

# If the checkbox is checked, show the element
if show_element:
    st.write("This element is visible when the checkbox is checked.")
else:
    st.write("This element is hidden when the checkbox is not checked.")
