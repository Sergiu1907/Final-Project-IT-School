from crypto import Crypto_APP
import datetime  as dt
import os
from fpdf import FPDF

symbol ="btc"  
currency = "BUSD"
interval = "1d"  
dt_start = str (int(dt.datetime(2021,8,10).timestamp()*1000))
dt_end = str (int(dt.datetime(2022,8,29).timestamp()*1000))

if not os.path.exists("images"):
    os.mkdir("images")

coin = Crypto_APP(symbol.upper(), currency.upper(), dt_start, dt_end, interval)
coin.get_crypto_content()
coin.get_plot_price()
coin.get_plot_volume()
coin.get_pdf_raport()



















# r = requests.get(f'{base_URL}/klines?symbol={symbol}{currency}&interval={interval}&startTime={dt_Start}&endTime={dt_End}&limit=1000')
# content = json.loads(r.content)

# pd_content = pd.DataFrame(content)

# final_content = pd_content.iloc[:,0:6]
# final_content.columns = ("Start Time", "Open Price", "High", "Low", "Close Price","Close Time", "Volume", "Trades")




# class Crypto_Main:
#     def __init__(self, symbol):
#         self.symbol = symbol
#         self.currency = currency




# class user_data:
#     def add_crypto_data():
#         return {
#             "symbol": input ("Enter Crypto symbol:"),
#             "currency":input ("Chose currency:"),
#             "Start_Date":input("Enter start date:"),
#             "End_Date": input ("Enter end date:"),
#             "Interval": input ("Chose an interval:")
#         }



# # df_columns = ["open_time", "close_time", "open_price", "highest_price", "lowest_price", "close_price", 
# #             "volume", "num_trades"]







# try:
#     #1 facem request
#     response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")

# except requests.exceptions.RequestException as err:
#     print (err)
# else:
#     #2 Verificam status code sa fie 200
#     if response.status_code == 200:
#         # data =json.loads(response.content)
#         data = response.json()
#         print (data)
#     #3 Extragem datele
#     else:
#         print(response.content)

