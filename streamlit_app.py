# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection

import pandas as pd
import numpy as np
import yt_comment_req
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode
import streamlit as st


# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
def pageTest():
    my_dict = {}
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
        #st.write(vidID)
        my_dict = yt_comment_req.get_youtube_comments(vidID)

    # Below will have code regarding language processing
    # constructor
    # pass the text 
    # this document constructor has several elements. content, language_code, and type
    # Get the sentiments of the comments
    #st.write (len(my_dict.keys()))
    value_index = 0
    sentiments = []
    
    arr = list(my_dict.keys())
    for key in arr: # assuming comments_text is an array / hashmap
        for value in arr:
            valueString = str(value)
            sentiment = get_sentiment(valueString)
            sentiments.append(sentiment)
        value_index += 1
        
        
    value_ind = 0
    for key in my_dict.keys(): # assuming comments_text is an array / hashmap
        #st.write(key)
        for value in my_dict.get(key):
            valueString = str(value)
        value_ind += 1
    render_stacked_line_chart(arr, sentiments)



   # for sentiment in sentiments:

        #here in this loop we will append values to the graph

        
    #print("Sentiment: {}, {}".format(sentiment[sentiment_index].score, sentiment[sentiment_index].magnitude))

    # We can use the client. object methods for more data analysis

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

    return score

def render_stacked_line_chart(arr, sentiArr):
    options = {
        "title": {"text": "Sentiment Value of Recent Videos"},
        "tooltip": {"trigger": "axis"},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": arr,
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "name1",
                "type": "line",
                "stack": "stack1",
                "data": sentiArr,
            },
        ],
    }
    st_echarts(options=options, height="400px")