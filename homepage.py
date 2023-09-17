import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#Make sure to: 
#   - pip install streamlit-option-menu
#   - pip install streamlit_lottie


st.set_page_config(page_title="My Webpage", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
    )

#st.markdown("""<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
#            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
#            crossorigin="anonymous">""", unsafe_allow_html=True)

#with open("homepageStyle.css") as f:
#    css = f.read()
#    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

#st.markdown("""
#<nav class="navbar navbar-expand-lg navbar-light bg-light">
#  <a class="navbar-brand" href="#">Navbar</a>
#  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#    <span class="navbar-toggler-icon"></span>
#  </button>
#
#  <div class="collapse navbar-collapse" id="navbarSupportedContent">
#    <ul class="navbar-nav mr-auto">
#      <li class="nav-item active">
#        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
#      </li>
#      <li class="nav-item">
#        <a class="nav-link" href="#">Link</a>
#      </li>
#     <li class="nav-item dropdown">
#       <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
#          Dropdown
#        </a>
#        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
#          <a class="dropdown-item" href="#">Action</a>
#          <a class="dropdown-item" href="#">Another action</a>
#          <div class="dropdown-divider"></div>
#          <a class="dropdown-item" href="#">Something else here</a>
#        </div>
#      </li>
#      <li class="nav-item">
#        <a class="nav-link disabled" href="#">Disabled</a>
#      </li>
#    </ul>
#    <form class="form-inline my-2 my-lg-0">
#      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
#      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
#    </form>
#  </div>
#</nav>
#""", unsafe_allow_html=True)

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