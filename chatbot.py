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


df = pd.read_csv('https://raw.githubusercontent.com/Kim-Jun-Hee/sejong/main/food.csv', encoding='utf-8')
age_rankings_df = pd.read_csv("https://raw.githubusercontent.com/Kim-Jun-Hee/sejong/main/agegender.csv",encoding='utf-8')


