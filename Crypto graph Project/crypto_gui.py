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

    print (day_s, month_s, year_s)
    print (day_e, month_e, year_e)


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

# def submit2():
#     coin_symbol = entry.get()
#     coin_currency = entry2.get()
#     symbol =coin_symbol  
#     currency = coin_currency
#     print(symbol)
#     print(currency)
    # interval = "1d"  
    # dt_start = str (int(dt.datetime(2021,8,10).timestamp()*1000))
    # dt_end = str (int(dt.datetime(2022,8,29).timestamp()*1000))

    # if not os.path.exists("images"):
    #     os.mkdir("images")

    # coin = Crypto_APP(symbol.upper(), currency.upper(), dt_start, dt_end, interval)
    # coin.get_crypto_content()
    # coin.get_plot_price()
    # coin.get_plot_volume()
    # coin.get_pdf_raport()


# submit_button2 = Button(crypto_box, text = "Subit currency", command=submit2)
# submit_button2.pack(side=RIGHT)

# symbols_list_box = (lists_frame, bg="#f7ffde")
# symbols_list_box.grid(row=1,column=0)

# currency_list_box = Listbox(lists_frame, bg="#f7ffde")
# currency_list_box.grid(row=1,column=1)




# crypto_list_box = Listbox(
#                         symbol_list_frame,
#                         bg = "#f7ffde",
#                         font=("Constantia",12)
#                         )

# currency_list_box = Listbox(list_frame,                        
#                             bg = "#f7ffde",
#                             font=("Constantia",12)
#                         )
                            
# crypto_list_box.grid(row=0,column=0)
# currency_list_box.grid(row=0,column=1, padx= 30)
                        
# symbol_list = sorted["BTC", "ETH", "BNB", "XRP", "ADA", "DOGE", "DOT", "SOL", "MATIC"]
# for i in sorted(symbol_list):
#     crypto_list_box.insert(END, i)

# currency_list_box.insert(END, "EUR")
# currency_list_box.insert(END, "USDT")



# currency_list_box = Listbox(crypto_box, justify= LEFT,
#                         name="currency",
#                         bg = "#f7ffde",
#                         font=("Constantia",14))
# currency_list_box.pack(pady=15)




# entry = Entry(crypto_box,
#             font=("Arial",20))
# entry.pack(side=LEFT)
# entry2 = Entry(crypto_box,
#             font=("Arial",20))
# entry2.pack(side=LEFT)
# submit_button2 = Button(crypto_box, text = "Subit currency", command=submit2)
# submit_button2.pack(side=RIGHT)





# box = Tk()
# box.withdraw()

# symbol = simpledialog.askstring (title="Symbol",
#                         prompt="Chose a symbol" )

# currency = simpledialog.askstring (title="Currency",
#                         prompt="Chose a currency" )

# print("Hello" + symbol+currency) 

