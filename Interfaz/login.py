# login.py
import streamlit as st
from main import main  # Import the main function

def login():
    st.title("Login")

    # Input fields for email and password
    email = st.text_input("Email:")
    password = st.text_input("Contrasenia:", type="password")

    # Check if login button is pressed
    if st.button("Login"):
        # You can implement your own validation logic here
        if email == "a" and password == "a":
            st.success("Login Successful!")
            # Clear the login page and display the main page
            st.empty()
            main()
        else:
            st.error("usuario o contrasenia inc")
    
    return False


st.sidebar.success("test")

if __name__ == "__main__":
    login()


