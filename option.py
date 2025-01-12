'''
import streamlit as st

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
    st.markdown("<h3 style='text-align: center;'>Find Some Foods You Can Make Now!</h3>", unsafe_allow_html=True)
    st.image("photo2.jpg", width=400)
    if st.button("Find foods you can make now!", use_container_width=True):
        st.write("You selected Option 2")
'''