from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import requests
import json

class Crypto_APP:
    def __init__ (self, symbol, currency, dt_start, dt_end, interval):
        self.symbol = symbol
        self.currency = currency
        self.dt_start = dt_start
        self.dt_end = dt_end
        self.interval = interval
        self.price_list = []


    def get_crypto_content(self):
        BASE_URL = "https://api.binance.com/api/v3"
        r = requests.get(f'{BASE_URL}/klines?symbol={self.symbol}{self.currency}&interval={self.interval}&startTime={self.dt_start}&endTime={self.dt_end}&limit=1000')
        content = json.loads(r.content)
        for i in content :
            price = Coin(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[8])
            self.price_list.append(price)
        

    def get_plot(self):
        list_close_time = []
        list_close_price = []
        for i in self.price_list:
            a = datetime.fromtimestamp((i.close_time)/1000.0)
            list_close_time.append(a.strftime('%Y-%m-%d'))
            # list_close_time.append(i.close_time)
            list_close_price.append(i.close_price)
        get_date = datetime.now()
        generate_date = get_date.strftime('%Y-%m-%d %H:%M:%S' )
        fig = px.line(
            x = list_close_time  , y = list_close_price, labels= {"x":"Date", 'y':f'{self.currency}'},
            title = f'Crypto raport: {self.symbol}-{self.currency} {generate_date}'
            )
        # print (list_close_price) 
        # print(list_close_time)
        return fig.show()
        # fig.write_image (f'images/{self.symbol}{self.currency}.png')


class Coin:
    def __init__ (self, open_time, open_price, high_price, low_price, close_price, volume, close_time, trades):
        self.open_time = open_time
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = float(close_price)
        self.volume = volume
        self.close_time = close_time
        self.trades = trades



















    # def __str__(self):
    #     return str(self.open_time) +" "+ str(self.open_price)  +" "+ str(self.high_price) +" "+ str(self.low_price) +" "+ str(self.close_price) +" "+ str(self.volume) +" "+ str(self.close_time) +" "+ str(self.trades)


# list1= []
#             list1.append(i[0])
#             list1.append(i[1])
#             list1.append(i[2])
#             list1.append(i[3])
#             list1.append(i[4])
#             list1.append(i[5])
#             list1.append(i[6])
#             list1.append(i[8])



# def get_graph(self,list):
    #     df = pd.DataFrame(list)
    #     df.columns = ["Start Date", "Open Price", "High Price", "Low Price", "Close Price", "Volume", "Close Date", "Trades"]
    #     return df

        # df =pd.DataFrame(content)
        # df = df.iloc[:,0:9]
        # df.columns = ["Start Date", "Open Price", "High Price", "Low Price", "Close Price", "Volume", "Close Date", "7", "Trades"]
        # return df 