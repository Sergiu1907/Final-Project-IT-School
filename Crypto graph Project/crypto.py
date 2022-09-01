from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import requests
import json
from fpdf import FPDF

class Crypto_APP:
    def __init__ (self, symbol, currency, dt_start, dt_end, interval):
        self.symbol = symbol
        self.currency = currency
        self.dt_start = dt_start
        self.dt_end = dt_end
        self.interval = interval
        self.price_list = []
        self.list_close_time =[]
        self.list_close_price =[]
        self.list_volume = []
        self.list_trades = []

    def get_crypto_content(self):
        BASE_URL = "https://api.binance.com/api/v3"
        r = requests.get(f'{BASE_URL}/klines?symbol={self.symbol}{self.currency}&interval={self.interval}&startTime={self.dt_start}&endTime={self.dt_end}&limit=1000')
        content = json.loads(r.content)
        for i in content :
            price = Coin(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            self.price_list.append(price)
        

    def get_plot_price(self):
        for i in self.price_list:
            a = datetime.fromtimestamp((i.close_time)/1000.0)
            self.list_close_time.append(a.strftime('%Y-%m-%d'))
            self.list_close_price.append(i.close_price)     
        get_date = datetime.now()
        generate_date = get_date.strftime('%d-%m-%Y %H:%M:%S' ) 
        fig = px.line(
            x = self.list_close_time  , y = self.list_close_price, labels= {"x":"Date", 'y':f'{self.currency}'},
            title = f'Crypto raport: {self.symbol}-{self.currency} {generate_date}'
            )
        return fig.write_image (self.get_f_string('Price'))


    def get_date(self,date):
        formated_date = datetime.fromtimestamp(int(date)/1000)
        date_final = formated_date.strftime('%d_%m_%Y')
        return date_final

    def get_max_price(self):
        coin_price = []
        for i in self.price_list:
            coin_price.append(i.close_price)
        max_price = max(coin_price)
        return max_price

    def get_min_price(self):
        coin_price = []
        for i in self.price_list:
            coin_price.append(i.close_price)
        min_price = min(coin_price)
        return min_price

    def get_plot_volume(self):
        for i in self.price_list:
            self.list_volume.append(i.volume)
            self.list_trades.append(i.trades)
        fig = px.bar (
            x = self.list_close_time  , y = self.list_volume, labels= {"x":"Date", 'y':'Volume'},
            title = f'Crypto volume raport: {self.symbol}-{self.currency}, Total volume: {self.get_sum_volume_trades(self.list_volume)}'
            )
        return fig.write_image (self.get_f_string('Volume'))

    def get_sum_volume_trades(self,list):
        sum_volume_trades =  sum (list)
        return sum_volume_trades

    def get_f_string(self, name):
        string = f'images\{name}_{self.symbol}_{self.currency} {self.get_date(self.dt_start)}-{self.get_date(self.dt_end)}.png'
        return string

    def get_pdf_raport(self):
        pdf = FPDF('P','mm', 'A4')
        pdf.add_page()
        pdf.set_font('times','',12)
        pdf.text(20,119,f'Max Price: {self.get_max_price()} {self.currency}')
        pdf.text(20,125,f'Min Price: {self.get_min_price()} {self.currency}')
        pdf.text(20,250,f'Total volume: {self.get_sum_volume_trades(self.list_volume)}')
        pdf.text(20,260,f'Total trades: {self.get_sum_volume_trades(self.list_trades)}')
        pdf.image(self.get_f_string("Price"),10,0,160)
        pdf.image(self.get_f_string("Volume"),10,130,160)
        pdf.output(f'Raport {self.symbol}{self.currency} {self.get_date(self.dt_start)}-{self.get_date(self.dt_end)}')


class Coin:
    def __init__ (self, open_time, open_price, high_price, low_price, close_price, volume, close_time, total_transact, trades):
        self.open_time = open_time
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = float (close_price)
        self.volume = float (volume)
        self.close_time = close_time
        self.total_transact = total_transact
        self.trades = int (trades)