import streamlit as st

# Function to inject custom CSS
def inject_custom_css():
    st.markdown(
        """
        <style>
        /* Global styling */
        body {
            font-family: Arial, sans-serif;
        }
        
        /* Start Page Styling */
        .start-container {
            position: relative;
            text-align: center;
            color: white;
            padding: 100px 0;
        }

        .start-container h1 {
            font-size: 4rem;
            margin-bottom: 20px;
        }

        .start-container p {
            font-size: 1.5rem;
            margin-bottom: 40px;
        }

        .start-button {
            font-size: 1.25rem;
            padding: 15px 30px;
            cursor: pointer;
            border: none;
            background-color: #008CBA;
            color: white;
            border-radius: 10px;
            transition: 0.3s ease;
        }

        .start-button:hover {
            background-color: #005f73;
        }

        /* Parallax effect */
        .parallax {
            background-image: url('https://source.unsplash.com/1600x900/?nature,water');
            height: 100%;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            position: relative;
        }

        /* About Page Styling */
        .about-container {
            padding: 50px;
            background-color: #f2f2f2;
            text-align: center;
        }

        .about-container h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .about-container p {
            font-size: 1.2rem;
            margin-bottom: 40px;
        }

        </style>
        """, unsafe_allow_html=True
    )