# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection

import pandas as pd
import numpy as np

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
def pageTest():
    conn = st.experimental_connection('gcs', type=FilesConnection)
    df = conn.read("smuv-bucket/myfile.csv", input_format="csv", ttl=600)

    st.title("Youtube Channel Comment Trends")

    # Input field for Youtube URL
    url = st.text_input('Enter Youtube Channel URL')

    st.write(url)

    with open("yt_comment-req.py") as f:
        exec(f.read())

    #
    # Below will have code regarding language processing
    from google.cloud import language_v1
    # constructor
    client = language_v1.LanguageServiceClient()

    text = u"""Sample text"""
    # document object from language v1 library
    document = language_v1.Document(
    # pass the text 
    # this document constructor has several elements. content, language_code, and type
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
    # We can use the client. object methods for more data analysis

    # print data to website
    st.header("Sentiment Value of Recent Videos")
