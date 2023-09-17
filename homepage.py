import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#Make sure to: 
#   - pip install streamlit-option-menu
#   - pip install streamlit_lottie


st.set_page_config(page_title="My Webpage", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("homepageStyle.css")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Analytics", "Contacts"],
        icons=["house", "clipboard2-data-fill", "envelope-at"]
    )

if selected == "Home":
    with st.container():
        st.title("The man from Mi-dang")
        st.write("Here's a topato")
        st.write("[Learn More >](https://themodernproper.com/30-best-potato-recipes)")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("This is the left column")
            st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                    dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
                    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
        with right_column:
            st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                    dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
                    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")

if selected == "Contacts":
    with st.container():
        st.write("---")
        st.header("Get in touch with us!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/siryeetthrowaway@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()