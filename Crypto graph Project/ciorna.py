from time import strftime
import plotly.express as px
import plotly.graph_objects as go
import pathlib
import os
from datetime import datetime
import requests
import json


symbol ="BTC"  
currency = "BUSD"
interval = "1d"  
dt_start = str (int(datetime(2022,8,13).timestamp()*1000))
dt_end = str (int(datetime(2022,8,25).timestamp()*1000))


BASE_URL = "https://api.binance.com/api/v3"
r = requests.get(f'{BASE_URL}/klines?symbol={symbol}{currency}&interval={interval}&startTime={dt_start}&endTime={dt_end}&limit=1000')
content = json.loads(r.content)

def get_max_price():
    list_close_price = [1,4,3,7,5,9]
    max_price = max(list_close_price)
    return max_price

print (get_max_price())












# fig = px.line(x=[1661119199999, 1661122799999, 1661126399999, 1661129999999, 1661133599999 ], y=[21461.16000000, 21505.00000000, 21538.04000000, 21480.29000000, 21416.00000000])
# root_dir = pathlib.Path(__file__).parent

# if not os.path.exists("images"):
#     os.mkdir("images")

# fig.write_image("images/test2.png")
# # Creating the Figure instance
# # fig.write_image("fig.png") # save as test.png


