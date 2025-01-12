import pyrebase
import streamlit as st
import time
import os

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

import streamlit as st

def inject_custom_css(image_path):
    st.markdown(
        f"""
        <style>
        /* Global styling */
        body {{
            font-family: Arial, sans-serif;
        }}
        
        /* Start Page Styling */
        .start-container {{
            position: relative;
            text-align: center;
            color: white;
            padding: 100px 0;
        }}

        .start-container h1 {{
            font-size: 4rem;
            margin-bottom: 20px;
        }}

        .start-container p {{
            font-size: 1.5rem;
            margin-bottom: 40px;
        }}

        .start-button {{
            font-size: 1.25rem;
            padding: 15px 30px;
            cursor: pointer;
            border: none;
            background-color: #008CBA;
            color: white;
            border-radius: 10px;
            transition: 0.3s ease;
        }}

        .start-button:hover {{
            background-color: #005f73;
        }}

        /* Parallax effect */
        .parallax {{
            background-image: url('{image_path}');
            height: 100%;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            position: relative;
        }}

        /* About Page Styling */
        .about-container {{
            padding: 50px;
            background-color: #f2f2f2;
            text-align: center;
        }}

        .about-container h2 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
        }}

        .about-container p {{
            font-size: 1.2rem;
            margin-bottom: 40px;
        }}
        </style>
        """, unsafe_allow_html=True
    )

def about_page():
    st.markdown('<div class="about-container">', unsafe_allow_html=True)  # About page container
    st.header("About the App")
    st.write("""
    Our app is designed to provide seamless login and signup functionality.
    We aim to deliver a user-friendly experience with a beautiful interface, smooth transitions, and easy navigation.

    Features:
    - Secure login and sign-up process
    - Parallax scroll effect for an immersive experience
    - Intuitive design with clear navigation

    Feel free to explore and get started!
    """)
    st.markdown('</div>', unsafe_allow_html=True)


def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button('Login'):
        try:
            user = auth.sign_in_with_email_and_password(username,password)
            st.success("Login successful!")
            time.sleep(2.5)
            st.session_state.page = "menu" 
        except:
            st.error("Invalid Login Chief")
    if st.button('Back'):
        st.session_state.page = "start"

def signup():
    st.title("Signup Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button('Sign Up'):
        try:
            user = auth.create_user_with_email_and_password(username,password)
            st.success("Login successful!")
            st.session_state.page = "menu"
        except:
            st.error("Invalid signup gang")
    if st.button('Back'):
        st.session_state.page = "start"

def start_page(image_path):
    st.markdown('<div class="parallax"></div>', unsafe_allow_html=True)  # Parallax background
    
    st.markdown('<div class="start-container">', unsafe_allow_html=True)  # Start page container
    st.header("Welcome to Our App!")
    st.write("Scroll down to learn more about the app.")
    
    # Buttons for navigating to login/signup
    if st.button("Login", key="login", use_container_width=True):
        st.session_state.page = "login"  # Navigate to login page
    if st.button("Sign Up", key="signup", use_container_width=True):
        st.session_state.page = "signup"  # Navigate to signup page

    st.markdown('</div>', unsafe_allow_html=True)

def menu():
    st.markdown("<h1 style='text-align: center;'>What Would You Like To Do?</h1>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Add custom CSS for spacing between columns
    st.markdown("""
        <style>
            .css-1d391kg {
                margin-right: 30px;
            }
            .css-18e3th9 {
                margin-left: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='text-align: center;'>Take A Photo Of Your Food!</h3>", unsafe_allow_html=True)
        st.image("photo1.jpeg", width=400)
        if st.button("Take a photo of your food!", use_container_width=True):
            st.write("You selected Option 1")

    with col2:
        st.markdown("<h3 style='text-align: center;'>Make Some Food Now!</h3>", unsafe_allow_html=True)
        st.image("photo2.jpg", width=400)
        if st.button("Find foods you can make now!", use_container_width=True):
            st.session_state.page = "option2"

def option2():
    st.markdown("<h1 style='text-align: center;'>Here's A Quick Questionnaire</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### Do you have any dietary restrictions?")
    dietary_restrictions = st.radio(
        "Select any dietary restrictions:",
        ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free", "Other"]
)
    if dietary_restrictions == "Other":
        other_restriction = st.text_input("Specify your other dietary restriction:")

    st.markdown("### Do you have any specific food goals (e.g., cutting, bulking, maintaining)?")
    food_goals = st.text_input("Enter your food goals:")

    st.markdown("### What food items do you currently have access to that you want to use to make a meal?")
    available_foods = st.text_area("List the food items you have:")

    st.markdown("### What is your primary goal with your meals?")
    primary_meal_goal = st.radio(
        "Select your primary goal:",
        ["Weight loss", "Muscle gain", "Improved health", "Convenience", "Other"]
    )

    if primary_meal_goal == "Other":
        primary_meal_goal = st.text_input("Specify your other goal:")

    if st.button("Submit"):
        st.markdown("### Here's a summary of your answers:")
        st.write(f"Dietary restrictions: {dietary_restrictions} {'and ' + other_restriction if other_restriction else ''}")
        st.write(f"Food goals: {food_goals}")
        st.write(f"Available food items: {available_foods}")
        st.write(f"Meals per day: {primary_meal_goal}")


def main():
    if "page" not in st.session_state:
        st.session_state.page = "start"  

    image_path = "background2.avif"

    if os.path.exists(image_path):
        inject_custom_css(image_path)
        if st.session_state.page == "start":
            start_page(image_path)
        elif st.session_state.page == "about":
            about_page()
        elif st.session_state.page == "login":
            login()
        elif st.session_state.page == "signup":
            signup()
        elif st.session_state.page == "menu":
            menu()
        elif st.session_state.page == "option2":
            option2()
    else:
        st.error("Background image 'background.avif' not found in the 'images' folder.")

if __name__ == "__main__":
    main()