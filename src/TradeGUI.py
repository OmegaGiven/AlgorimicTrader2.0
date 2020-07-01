import tkinter as tk
from tkinter import ttk
import alpaca_trade_api as tradeapi
from src import AlpacaFunctions

f = open('API.txt', 'r')
if f.mode == 'r':
    file = f.read().split('\n')
f.close()
api = tradeapi.REST(file[0], file[1], file[2])

app = tk.Tk()
app.title('TradeGUI')


tab_menu = tk.ttk.Notebook(app)
home = tk.ttk.Frame(tab_menu)
trader = tk.ttk.Frame(tab_menu)
tab_menu.add(home, text='Home')
tab_menu.add(trader, text='Trader')

accountName = tk.Label(home, text='Account: ' + api.get_account().account_number)
accountName.grid(row=0)
amount_available = tk.Label(home, text='Available Money: ' + api.get_account().cash)
amount_available.grid(row=1, column=0)
equity = tk.Label(home, text='Equity: ' + api.get_account().equity)
equity.grid(row=2, column=0)


def MACDalgorithm():
    AlpacaFunctions.main('AMD')


MACDtext = tk.Label(home, text='Run MACD strategy: ')
MACDtext.grid(row=0)
MACDbutton = tk.Button(trader, text='MACD', command=MACDalgorithm)
MACDbutton.grid(row=0, column=1)





tab_menu.pack(expand=1, fill='both')
app.mainloop()
