# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection

import pandas as pd
import numpy as np
import yt_comment_req

my_dict = {}
# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
def pageTest():
    conn = st.experimental_connection('gcs', type=FilesConnection)
    df = conn.read("smuv-bucket/myfile.csv", input_format="csv", ttl=600)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("streamlit_app.css")


    st.title("Youtube Channel Comment Trends")

    st.title("")

    # Input field for Youtube URL
    channel_code = st.text_input('Enter Youtube Channel Code')
    if channel_code:
        # Gets playlist of all videos for a given channel
        uploads_id = yt_comment_req.get_uploads_from_channel_code(channel_code)
        # Gets array of first 10 video IDS
        videoIds = yt_comment_req.get_video_id_from_uploads(uploads_id)

        vidID = videoIds[0]
        st.write(vidID)
        my_dict = yt_comment_req.get_youtube_comments(vidID)

    value_ind = 0
    for key in my_dict.keys(): # assuming comments_text is an array / hashmap
        st.write(key)
        for value in my_dict.get(key):
            valueString = str(value)
        value_ind += 1

    yt_comment_req.render_stacked_line_chart()

    # Below will have code regarding language processing
    # constructor
    # pass the text 
    # this document constructor has several elements. content, language_code, and type
    # Get the sentiments of the comments
    #st.write (len(my_dict.keys()))
    value_index = 0
    sentiments = []
    for key in my_dict.keys(): # assuming comments_text is an array / hashmap
        for value in my_dict.get(key):
            valueString = str(value)
            sentiment = get_sentiment(valueString)
            sentiments.append(sentiment)
        value_index += 1

    for sentiment in sentiments:
        #here in this loop we will append values to the graph

        
    #print("Sentiment: {}, {}".format(sentiment[sentiment_index].score, sentiment[sentiment_index].magnitude))

    # We can use the client. object methods for more data analysis

# ========================   BELOW IS ALL TEST CODE   ========================
# I will try to create some modularity.
def get_sentiment(comment):

    from google.cloud import language_v1
    # Create a language client
    client = language_v1.LanguageServiceClient()
    

    # Create a document object
    document = language_v1.Document(content=comment, type_=language_v1.Document.Type.PLAIN_TEXT)
    #document.type = language.Document.Type.PLAIN_TEXT
    

    # Analyze the document
    response = client.analyze_sentiment(request={'document': document})
    

    # Get the sentiment score
    score = response.document_sentiment.score

    #comment these out later
    #st.write("score is ")
    #st.write(score)

    return score
