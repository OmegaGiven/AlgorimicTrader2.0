
import alpaca_trade_api as tradeapi

def getAccount():
    f = open('API.txt', 'r')
    if f.mode == 'r':
        file = f.read().split('\n')
    f.close()
    api = tradeapi.REST(file[0], file[1], file[2])
    return api

# checks account from API. txt so you will need the 2 security keys and the route

