import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", layout="wide")

#def load_lottieurl(url):
#    r = requests.get(url)
#    if r.status_code != 200:
#        return None
#    return r.json()

with st.container():
    st.subheader("Welcome to Python")
    st.title("The man from Mi-dang")
    st.write("Here's a topato")
    st.write("[Learn More >](https://themodernproper.com/30-best-potato-recipes)")

#lottieGif = "https://lottie.host/7115e53b-06b5-4d1b-89b6-e6099b2e04eb/A3KlROtFcn.json"

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
        #st_lottie(lottieGif, height=300, key="gif")

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="text" name="name" required>
        <input type="email" name="email" required>
        <button type="submit">Send</button>
    </form> 
    """


st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )