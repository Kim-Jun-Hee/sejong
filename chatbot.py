import streamlit as st
import time
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
import requests
from streamlit_chat import message
import urllib3
import json
import base64
import re
 


# 데이터 불러오기 cp949
df = pd.read_csv('https://raw.githubusercontent.com/Kim-Jun-Hee/sejong/main/음식점정보홈페이지활용_메뉴최종.csv', encoding='utf-8')
age_rankings_df = pd.read_csv("https://raw.githubusercontent.com/Kim-Jun-Hee/sejong/main/나이대성별선호음식순위.csv",encoding='utf-8')


