import pyrebase
import streamlit as st
import time
import os
import json
import cohere 
from PIL import Image
import ollama
import io
import tempfile

co = cohere.ClientV2(api_key="bySl2q8fIzNgKJrAR1IRAVKQhwgPdGzyD9eqclt2")

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

message_configuration = """Style Guide
First list out the name of the dish and its ingredients
Second list the instructions on how to cook the recipe
Lastly only list out the number of calories and protein of the meal
Using this structure create only 3 recipes
Make the recipe titles bold and bigger than the rest of the text
Number the recipes and do not use any hashtags in the response
State whether the recipe can be made with the available food items or not
"""


message_structure = """This is how the response should be structured, follow this format exactly:
Recipe 1: Chicken and Vegetable Pasta

Ingredients:
- 2 boneless, skinless chicken breasts, cut into bite-sized pieces
- 1 medium onion, diced
- 2 bell peppers (any color), sliced
- 200g pasta noodles (penne, fusilli, or your choice)
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon Italian seasoning
- Salt and pepper to taste
- Grated Parmesan cheese for serving (optional)

Instructions:
1. Cook pasta according to package instructions in salted water until al dente. Drain and set aside.
2. Heat olive oil in a large skillet over medium-high heat. Add the diced onion and sliced bell peppers. Sauté for about 5 minutes until the vegetables start to soften.
3. Add the minced garlic and Italian seasoning to the skillet, cooking for another minute while stirring frequently.
4. Place the chicken pieces into the skillet and cook for 6-8 minutes, stirring occasionally, until the chicken is cooked through and no longer pink.
5. Return the cooked pasta to the skillet and toss everything together until well combined. Season with salt and pepper to taste.
6. Serve the pasta dish with grated Parmesan cheese on top, if desired.

Nutrition Information (per serving):
    Calories: Approximately 550 calories
    Protein: 35g
    Fat: 28g
    Carbohydrates: 40g
    Sugar: 5g
"""


st.markdown(
    """
    <style>
    .custom-header {
        font-family: 'Dancing Script', cursive !important; 
        font-size: 36px !important; 
        color: #2E8B57; 
        text-align: center;
        margin-top: -50px;  
    }
    </style>
    <p class="custom-header">Track Smarter. Eat Better. Live Healthier.</p>
    """,
    unsafe_allow_html=True
)

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
            margin-top: -210px;
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
    col1, col2 = st.columns([1, 1])

    col1.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
    .custom-header {
        font-family: 'Lato', serif;
        font-size: 30px !important;  
        color: #2E8B57;  
        text-align: center;
        margin-top: -50px;  
    }
    </style>
    <p class="custom-header">What is MacroSpace? 🤔</p>
    """,
    unsafe_allow_html=True
    )
    col1.image('person.png')
    col2.text('''
              Key Features:
                🍽️ AI-Powered Macro Tracking – Instantly analyze your meals by snapping a photo.
                📝 Personalized Meal Plans – Custom recommendations based on your goals and preferences.
                🥗 Dietary Flexibility – Accommodates all diets, from vegan to keto.
                📊 Progress Tracking – Monitor your nutrition and fitness goals in one place.
                🤖 Smart Insights – AI-driven suggestions to optimize your health journey.
              ''')

    st.markdown('</div>', unsafe_allow_html=True)

    st.text('''
            MacroSnap is your all-in-one nutrition companion designed to make tracking your diet effortless 
            and accurate. Powered by advanced AI from Cohere, MacroSnap personalizes your health journey with 
            smart recommendations tailored to your food goals, dietary restrictions, and weight objectives.

            Snap a photo of your meal, and let MacroSnap analyze your macros in seconds—no manual logging needed! 
            Whether you're aiming to lose weight, build muscle, or maintain a balanced diet, MacroSnap empowers you with 
            actionable insights to make healthier choices.

            ''')



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

def start_page():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image('logo-removebg-preview.png',width=300)
    st.markdown('<div class="start-container">', unsafe_allow_html=True)  
    st.header("Welcome to MacroSnap!", divider="green")
    st.write("Scroll down to learn more about the app.")
    
    if st.button("Login", key="login", use_container_width=True):
        st.session_state.page = "login"  
    if st.button("Sign Up", key="signup", use_container_width=True):
        st.session_state.page = "signup" 

    st.markdown('</div>', unsafe_allow_html=True)
    about_page()

def menu():
    st.markdown("<h1 style='text-align: center;'>What Would You Like To Do?</h1>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

 
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
            st.session_state.page = "option1"

    with col2:
        st.markdown("<h3 style='text-align: center;'>Make Some Food Now!</h3>", unsafe_allow_html=True)
        st.image("photo2.jpg", width=400)
        if st.button("Find foods you can make now!", use_container_width=True):
            st.session_state.page = "option2"

def option1():
    camera_photo = st.camera_input("Take a food!")
    
    if camera_photo is not None:
        img = Image.open(camera_photo)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            img.save(temp_file, format="PNG")
            temp_file_path = temp_file.name
        
        res = ollama.chat(
            model='llava:7b',
            messages=[
                {
                    'role': 'user',
                    'content': 'Identify this food item.',
                    'images': [temp_file_path]
                }
            ]
        )
        if 'message' in res:
            identified_food = res['message']['content']
            st.session_state['identified_food'] = identified_food
            if st.button("Let's go", key="AI_response_opt1", use_container_width=True):
                st.session_state.page = "AI_response_opt1"
        else:
            st.write("No response from Ollama.")
    ##else:
        #st.write("Please take a photo first.")


user_inputs = []
def option2():
    if "user_inputs" not in st.session_state:
        st.session_state.user_inputs = []

    st.markdown("<h1 style='text-align: center;'>Here's A Quick Questionnaire</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### Do you have any dietary restrictions?")
    dietary_restrictions = st.radio(
        "Select any dietary restrictions:",
        ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free", "None", "Other"]
    )
    other_restriction = ""
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
        st.session_state.user_inputs = [
            f"Dietary Restrictions: {dietary_restrictions} {'and ' + other_restriction if other_restriction else ''}",
            f"Food Goals: {food_goals}",
            f"Available Food Items: {available_foods}",
            f"Primary Meal Goal: {primary_meal_goal}",
        ]

        st.success("Responses Submitted Successfully!")
        st.session_state.page = "AI_response"

def AI_response():
    if "user_inputs" not in st.session_state or len(st.session_state.user_inputs) < 4:
        st.error("Not enough user inputs available. Please complete the questionnaire.")
        if st.button("Go Back"):
            st.session_state.page = "option2"
        return

    user_inputs = st.session_state.user_inputs

    st.markdown("<h1 style='text-align: center;'>Food You Can Eat</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    message = f"""Can you make a healthy recipe using these user inputs: 
    
            {user_inputs[1]} 
            {user_inputs[2]}
            {user_inputs[0]}
            {user_inputs[3]}
            """
    response = co.chat(
    model="command-r-plus-08-2024",
    messages=[{"role": "system", "content": message_configuration},{"role": "system", "content": message_structure},{"role": "user", "content": message},],

    )
    st.markdown(response.message.content[0].text)

    if st.button("Back to Menu"):
        st.session_state.page = "menu"

prompt_message = f"""
    Please provide the nutrition facts for the food item you identified.
    First name the food item
    Next state the serving size of the food item
    Then provide the calories of the food item 
    Then provide the rest of the nutrition facts
    """

prompt_structure = f"""
    This is how the response should be structured, follow this format exactly:
    Item Name: Bear Paws  
    - Serving Size: 1 Pouch (40g)
    - Calories: 170
    
    Nutrient Content Per Serving:  
    - Total Fat: 5g
    - Total Carbohydrate: 27g
    - Sugars: 13g
    - Protein: 3g
    """

def AI_response_opt1():
    if 'identified_food' not in st.session_state or not st.session_state['identified_food']:
        st.error("No food item detected. Please take a photo first.")
        if st.button("Go Back"):
            st.session_state.page = "option1"
        return

    st.markdown("<h1 style='text-align: center;'>Nutrition Facts 📊</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {"role": "user", "content": prompt_message},{"role": "user", "content": prompt_structure}],
    )
    nutrition_info = response.message.content[0].text
    st.markdown(nutrition_info)

    if st.button("Back to Menu"):
        st.session_state.page = "menu"

def main():
    if "page" not in st.session_state:
        st.session_state.page = "start"  

    image_path = "background2.avif"

    if os.path.exists(image_path):
        inject_custom_css(image_path)
        if st.session_state.page == "start":
            start_page()
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
        elif st.session_state.page == "AI_response":
           AI_response()
        elif st.session_state.page == "option1":
            option1()
        elif st.session_state.page == "AI_response_opt1":
            AI_response_opt1()
    else:
        st.error("Background image 'background.avif' not found in the 'images' folder.")


if __name__ == "__main__":
    main()
