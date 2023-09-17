# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('gcs', type=FilesConnection)
df = conn.read("smuv-bucket/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} loves :{row.Pet}:")

# Input field for Youtube URL
st.text_input('Enter some text')

# I love cheeseburgers