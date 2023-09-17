import streamlit as st
import streamlit_app
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#Make sure to: 
#   - pip install streamlit-option-menu
#   - pip install streamlit_lottie
#   - pip install requests

def main():
    
    st.set_page_config(page_title="My Webpage", layout="wide")

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("homepageStyle.css")

    def gif_Loader(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    #youtubeGif = gif_Loader("https://lottie.host/a820c77a-f479-4a05-bf1c-1ec13193966d/VguKLow6eC.json")

    with st.sidebar:
        selected = option_menu(
            menu_title="",
            options=["Home", "Analytics", "Contacts"],
            icons=["house", "clipboard2-data-fill", "envelope-at"]
        )

    if selected == "Home":
        with st.container():
#           st_lottie(youtubeGif, height=100, key="coding")
            st.title("Youtube Analytics")

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader("Our Mission")
                st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
                        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
            with right_column:
                st.subheader("\n\n\n")
                st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
                        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
                
    if selected == "Analytics":
        streamlit_app.pageTest()

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

if __name__ == "__main__":
    main()