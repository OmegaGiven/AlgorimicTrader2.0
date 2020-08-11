'''
provided by https://medium.com/@jouneidraza522/yahoo-finance-api-to-get-stocks-tickers-data-in-python-c49820249a18
'''
from pandas_datareader import data as pdr
from datetime import date
import datetime
import yfinance as yf
yf.pdr_override()
import pandas as pd
# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list = ['AMD']
today = date.today()
# We can get data by our choice by giving days bracket
start_date = datetime.datetime(2019, 8, 11)
end_date = datetime.datetime(2020, 8, 11)
files=[]
def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname = ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)


# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv(filename+'.csv')


# This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
for tik in ticker_list:
    getData(tik)
