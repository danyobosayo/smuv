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

        # loop through videoIds
        for vidID in videoIds:
            temporary_dict = yt_comment_req.get_youtube_comments(vidID)
            for key in temporary_dict.keys():
                if key not in my_dict.keys():
                    my_dict[key] = temporary_dict[key]
                else:
                    for value in temporary_dict[key]:
                        my_dict[key].append(value)


    # Below will have code regarding language processing
    # constructor
    # pass the text 
    # this document constructor has several elements. content, language_code, and type
    # Get the sentiments of the comments
    #st.write (len(my_dict.keys()))

    sentiments = []
    
    
    arr = list(my_dict.keys())
    
    for key in arr: # assuming comments_text is an array / hashmap
        value_sum = 0
        size_of_value_array = len(my_dict[key])
        for value in my_dict[key]:
            valueString = str(value)
            sentiment = get_sentiment(valueString)
            value_sum += sentiment
        #take average
        average = value_sum / size_of_value_array
        sentiments.append(average)

    #st.write(my_dict.keys())
    #st.write(sentiments)

    graph_data_array = []
    local_arr_index = 0
    for key in my_dict.keys():
        local_arr = [key, sentiments[local_arr_index]]
        local_arr_index += 1
        graph_data_array.append(local_arr)
    
    #st.write(graph_data_array)
    
    

    #render_stacked_line_chart(arr, sentiments)
    render_stacked_line_chart(graph_data_array)


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

def render_stacked_line_chart(data):
    options = {
        "title": {"text": "Sentiment Value of Recent Videos"},
        "tooltip": {"trigger": "axis"},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "time",
            "boundaryGap": False,
            #"axisLabel": {
                #"formatter": '{yyyy}-{MM}-{dd}'
            #},
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "Sentiment Value",
                "type": "bar",
                "stack": "stack1",
                "data": data,
            },
        ],
    }
    st_echarts(options=options, height="400px")