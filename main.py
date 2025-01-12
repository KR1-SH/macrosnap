import pyrebase
import streamlit as st


firebaseConfig = {
  'apiKey': "AIzaSyB5utIbWGDdjJH9QpUCYp-L_kO219a5Ym0",
  'authDomain': "deltahacks2025-a77c1.firebaseapp.com",
  'projectId': "deltahacks2025-a77c1",
  'storageBucket': "deltahacks2025-a77c1.firebasestorage.app",
  'messagingSenderId': "985028244911",
  'databaseURL': "https://deltahacks2025-a77c1-default-rtdb.firebaseio.com/",
  'appId': "1:985028244911:web:65273a93c673c4cc882b5a",
  'measurementId': "G-RJP0R8KH83"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button('Login'):
        try:
            user = auth.sign_in_with_email_and_password(username,password)
            st.success("Login successful!")
        except:
            st.error("Invalid Login Chief")

def signup():
    st.title("Signup Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button('Sign Up'):
        try:
            user = auth.create_user_with_email_and_password(username,password)
            st.success("Login successful!")
        except:
            st.error("Invalid signup gang")

def start_page():
    st.title("Welcome to the App!")
    st.write("Please choose an option to proceed.")
    
    login_button = st.button("Login Here")
    signup_button = st.button("Sign Up Here")
    
    if login_button:
        st.session_state.page = "login" 
    elif signup_button:
        st.session_state.page = "signup"

def main():
    if "page" not in st.session_state:
        st.session_state.page = "start"  
    
    if st.session_state.page == "start":
        start_page()
    elif st.session_state.page == "login":
        login()
    elif st.session_state.page == "signup":
        signup()

if __name__ == "__main__":
    main()