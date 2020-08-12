from tkinter import Tk, Label, Button, Entry
from tkinter import ttk
from accountInfo import getAccount
from YahooHistoryDownloader import download

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
MACDtext = Label(trader, text='Run MACD strategy: ')
MACDtext.grid(row=0)
MACDbutton = Button(trader, text='MACD', )
MACDbutton.grid(row=0, column=1)


'''
Test History Tab menu
'''
# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
'''
    'AMD', 'TMUS', 'GPRO', 'BAC', 'FIT', 'GE', 'GERN', 'IGC', 'OGEN',
    'ZN', 'MTNB', 'NBEV', 'NEPT', 'AGRX', 'DTEA', 'VTVT', 'CGC', 'MSFT',
    'SQ', 'GRPN', 'AMD', 'NVDA', 'INTC', 'NTDOY', 'ATVI', 'CRON', 'IIPR',
    'ACB', 'TSLA'
'''
Symbol_list = []
dataText = ''
description_text_SYMBL = Label(testData, text="Enter SYMBOL of wanted data")
description_text_SYMBL.grid(row=1)


def inputData(SYMBOL, dataText):
    Symbol_list.append(SYMBOL.get())
    dataText += SYMBOL.get() + "\t"
    return dataText


def run(newData, dataText):
    dataText = inputData(newData, dataText)
    SYMBOL_Inventory = Label(testData, text=dataText)
    SYMBOL_Inventory.grid(row=3)


newData = Entry(testData)
newData.grid(row=1, column=1)
addButton = Button(testData, text='add', command=run(newData, dataText))
addButton.grid(row=1, column=2)


downloadButton = Button(testData, text='Download Yahoo Data', command=download(Symbol_list))
downloadButton.grid(row=2, column=1)


'''
packing the GUI to run
'''
tab_menu.pack(expand=1, fill='both')
app.mainloop()
