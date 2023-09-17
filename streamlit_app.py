# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection

import pandas as pd
import numpy as np
import yt_comment_req

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
def pageTest():
    conn = st.experimental_connection('gcs', type=FilesConnection)
    df = conn.read("smuv-bucket/myfile.csv", input_format="csv", ttl=600)

    st.title("Youtube Channel Comment Trends")

    st.title('could we get a small explanation with pictures on how to get your own channel code')

    # Input field for Youtube URL
    channel_code = st.text_input('Enter Youtube Channel Code')
    if channel_code:
       #Get uploads playlist's id
       uploads_id = yt_comment_req.get_uploads_from_channel_code(channel_code)
       st.write(uploads_id)

       #vidID = 
       #yt_comment_req.get_youtube_comments(vidID)

    yt_comment_req.render_stacked_line_chart()

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

# ========================   BELOW IS ALL TEST CODE   ========================
# I will try to create some modularity.
def get_sentiment(comment):
    from google.cloud import language
    from google.cloud.language import types
    # Create a language client
    client = language.LanguageServiceClient()

    # Create a document object
    document = types.Document()
    document.content = comment
    document.type = types.Document.Type.PLAIN_TEXT

    # Analyze the document
    response = client.analyze_sentiment(document)

    # Get the sentiment score
    score = response.document_sentiment.score

    return score

# Get the sentiments of the comments
sentiments = []
comments_text = []
for comment in comments_text: # assuming comments_text is an array / hashmap
    sentiment = get_sentiment(comment)
    sentiments.append(sentiment)
