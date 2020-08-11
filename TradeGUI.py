from tkinter import Tk, Label, Button
from tkinter import ttk
from accountInfo import getAccount
from menuFunctions import *

api = getAccount()

'''
GUI Creation
'''
theme = ["#00897b", "#00564d", "#282828", "#363636", "#969696"]
#   light_teal,      teal,      dark_grey,   grey,   light_grey
app = Tk()
app.title('TradeGUI')
tab_menu = ttk.Notebook(app)
home = ttk.Frame(tab_menu)
trader = ttk.Frame(tab_menu)
testData = ttk.Frame(tab_menu)
tab_menu.add(home, text='Home')
tab_menu.add(trader, text='Trader')
tab_menu.add(testData, text='Test Data')

'''
Home Tab menu
'''
accountName = Label(home, text='Account: ' + api.get_account().account_number)
accountName.grid(row=0)
amount_available = Label(home, text='Available Money: ' + api.get_account().cash)
amount_available.grid(row=1, column=0)
equity = Label(home, text='Equity: ' + api.get_account().equity)
equity.grid(row=2, column=0)

'''
Trader Tab menu
'''
MACDtext = Label(home, text='Run MACD strategy: ')
MACDtext.grid(row=0)
MACDbutton = Button(trader, text='MACD', command=MACDalgorithm)
MACDbutton.grid(row=0, column=1)


'''
Test History Tab menu
'''



'''
packing the GUI to run
'''
tab_menu.pack(expand=1, fill='both')
app.mainloop()
