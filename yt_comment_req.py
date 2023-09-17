import googleapiclient.discovery
import pandas as pd
import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBUf_aEux--I1a-R0Jlf1747KnHQ66x-JI"

def get_youtube_comments():
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId="WNrB1Q9Rry0",
        maxResults=100
    )
    response = request.execute()

    comments = []

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['updatedAt'],
            comment['likeCount'],
            comment['textDisplay']
        ])

def render_stacked_line_chart():
    options = {
        "title": {"text": "折线图堆叠"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "邮件营销",
                "type": "line",
                "stack": "总量",
                "data": [120, 132, 101, 134, 90, 230, 210],
            },
            {
                "name": "联盟广告",
                "type": "line",
                "stack": "总量",
                "data": [220, 182, 191, 234, 290, 330, 310],
            },
            {
                "name": "视频广告",
                "type": "line",
                "stack": "总量",
                "data": [150, 232, 201, 154, 190, 330, 410],
            },
            {
                "name": "直接访问",
                "type": "line",
                "stack": "总量",
                "data": [320, 332, 301, 334, 390, 330, 320],
            },
            {
                "name": "搜索引擎",
                "type": "line",
                "stack": "总量",
                "data": [820, 932, 901, 934, 1290, 1330, 1320],
            },
        ],
    }
    st_echarts(options=options, height="400px")


    #"https://echarts.apache.org/examples/en/editor.html?c=line-stack"