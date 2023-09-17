import googleapiclient.discovery
import pandas as pd
import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode
import streamlit as st

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBUf_aEux--I1a-R0Jlf1747KnHQ66x-JI"

def get_youtube_comments(vidID):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=vidID,
        maxResults=100,
        #Added parameters
        order="relevance"
    )
    response = request.execute()

    for item in response['items']:
        st.write(item['snippet']['topLevelComment']['snippet']['textDisplay'])

def render_stacked_line_chart():
    options = {
        "title": {"text": "Sentiment Value of Recent Videos"},
        "tooltip": {"trigger": "axis"},
 #       "legend": {"data": ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "name1",
                "type": "line",
#                "stack": "stack1",
                "data": [4,4.3,4],
            },
            {
                "name": "name2",
                "type": "line",
#                "stack": "stack2",
                "data": [5,3,2],
            },
        ],
    }
    st_echarts(options=options, height="400px")


    #"https://echarts.apache.org/examples/en/editor.html?c=line-stack"