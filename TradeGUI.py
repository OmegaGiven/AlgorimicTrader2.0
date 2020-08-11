import tkinter as tk
from tkinter import ttk
from accountInfo import getAccount
from menuFunctions import *

api = getAccount()

'''
GUI Creation
'''
app = tk.Tk()
app.title('TradeGUI')
tab_menu = tk.ttk.Notebook(app)
home = tk.ttk.Frame(tab_menu)
trader = tk.ttk.Frame(tab_menu)
tab_menu.add(home, text='Home')
tab_menu.add(trader, text='Trader')


'''
Home Tab menu
'''
accountName = tk.Label(home, text='Account: ' + api.get_account().account_number)
accountName.grid(row=0)
amount_available = tk.Label(home, text='Available Money: ' + api.get_account().cash)
amount_available.grid(row=1, column=0)
equity = tk.Label(home, text='Equity: ' + api.get_account().equity)
equity.grid(row=2, column=0)

'''
Trader Tab menu
'''
MACDtext = tk.Label(home, text='Run MACD strategy: ')
MACDtext.grid(row=0)
MACDbutton = tk.Button(trader, text='MACD', command=MACDalgorithm)
MACDbutton.grid(row=0, column=1)


'''
packing the GUI to run
'''
tab_menu.pack(expand=1, fill='both')
app.mainloop()
