import googleapiclient.discovery
import pandas as pd
import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode
import streamlit as st

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBUf_aEux--I1a-R0Jlf1747KnHQ66x-JI"

def get_uploads_from_channel_code(channel_code):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.channels().list(
        part="contentDetails",
        id=channel_code
    )
    response = request.execute()
    # issues here
    #st.write ("reponse item writing")
    #st.write(response['items'])
    for item in response['items']:
        return item['contentDetails']['relatedPlaylists']['uploads']

def get_video_id_from_uploads(uploads_id):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=uploads_id,
        maxResults=10
    )
    response = request.execute()

    videoIds = []

    for item in response['items']:
        videoIds.append(item['contentDetails']['videoId'])
    
    return videoIds

def get_youtube_comments(vidID):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=vidID,
        maxResults=100,
        #Added parameters
        order="relevance",
        textFormat="plainText"
    )
    response = request.execute()

    #Create hashmap that we will return
    my_dict = {}
    keys = []
    values = []

    #Code to print comments retrived
    for item in response['items']:
        values.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        commentDateString = item['snippet']['topLevelComment']['snippet']['publishedAt'].replace("-","")
        keys.append(commentDateString[:8])

    # Fill out the hash map 
    values_index = 0
    for key in keys: 
        if key not in my_dict.keys():
            my_dict[key] = []
            my_dict[key].append(values[values_index])
        else:
            my_dict[key].append(values[values_index])
        # increase index counter
        values_index = values_index + 1
    #st.write("Output in yt comment")
    #st.write (len(keys))

    return my_dict


    #"https://echarts.apache.org/examples/en/editor.html?c=line-stack"