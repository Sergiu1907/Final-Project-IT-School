from crypto import Crypto_APP
import datetime  as dt
import os
from fpdf import FPDF
from tkinter import *
from tkinter import ttk
from tkcalendar import *



crypto_window = Tk()
crypto_window.title("Crypto graph report")
crypto_window.geometry("500x300")

main_frame = Frame (crypto_window)
main_frame.pack()

lists_frame = LabelFrame(main_frame, text= "Crypto information")
lists_frame.grid(row=0, column=0)

symbol_list_frame = Label (lists_frame, text= "Crypto Symbol", font="Constantia")
symbol_list_frame.grid(row=0, column=0, padx=40)    
symbol_list = ["BTC", "ETH", "BNB", "XRP", "ADA", "DOGE", "DOT", "SOL", "MATIC"]
sorted_list = sorted (symbol_list) 
symbol_list_box = ttk.Combobox (lists_frame, values = sorted_list)
symbol_list_box.grid(row=1, column=0, pady=5)


currency_list_frame = Label (lists_frame, text= "Currency", font="Constantia" )
currency_list_frame.grid(row=0, column=1, padx=40)
currency_list = ttk.Combobox (lists_frame, values = ["EUR", "USDT"])
currency_list.grid(row=1, column=1, padx=25, pady=5)


calendar = DateEntry(lists_frame, selectmode='day', date_pattern = "dd/mm/y")
calendar.grid(row=3, column=0, pady=5)
cal_label = Label(lists_frame, text= "Choose start date", font="Constantia")
cal_label.grid(row=2, column=0, pady=5)


calendar2 = DateEntry(lists_frame, selectmode='day', date_pattern = "dd/mm/y")
calendar2.grid(row=3, column=1, pady=5)
cal_label2 = Label(lists_frame, text= "Choose end date", font="Constantia")
cal_label2.grid(row=2, column=1, pady=5)

def submit_data():
    symbol = symbol_list_box.get()
    currency = currency_list.get()
    start_date = calendar.get()
    end_date = calendar2.get()

    day_s = int(start_date[:2])
    month_s =int(start_date [3:5])
    year_s = int (start_date[6:10])

    day_e = int(end_date[:2])
    month_e =int(end_date [3:5])
    year_e = int (end_date[6:10])


    dt_start = str (int(dt.datetime(year_s,month_s,day_s).timestamp()*1000))
    dt_end = str (int(dt.datetime(year_e, month_e, day_e).timestamp()*1000))
    interval = "1d"
    if not os.path.exists("images"):
        os.mkdir("images")

    coin = Crypto_APP(symbol.upper(), currency.upper(), dt_start, dt_end, interval)
    coin.get_crypto_content()
    coin.get_plot_price()
    coin.get_plot_volume()
    coin.get_pdf_raport()



submit_button = Button(main_frame, text= "Submit", command=submit_data)
submit_button.grid(row=4, column=0, pady=15)



crypto_window.mainloop()



