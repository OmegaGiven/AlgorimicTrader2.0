import alpaca_trade_api as tradeapi

'''
This is meant to be used with cron tab so that it can run at the beginning or end
of the day, whichever you choose.
'''

# to set this up with your alpaca account create a file named 'API.txt'
# the file will contain 3 things 1; 'key', 2; 'secret key', 3; 'which market you want to trade paper or actual'
f = open('API.txt', 'r')
if f.mode == 'r':
    file = f.read().split('\n')
f.close()
api = tradeapi.REST(file[0], file[1], file[2])


def macd(symbol):
    bar_set = api.get_barset(symbol, 'day', limit=4)
    stock = bar_set[symbol]
    day1 = stock[0].c
    day2 = stock[1].c
    day3 = stock[2].c
    five_day_average = (day1 + day2 + day3) / 3
    current = stock[3].o
    if current > five_day_average:
        return 'buy'
    else:
        return 'sell'


def buy(symbol, quantity=1):
    f = open('History', 'a+')
    api.submit_order(symbol, quantity, 'buy', 'market', 'gtc')
    f.write('buying: ' + symbol + ' at ' + ' quantity: ' + str(quantity))
    f.close()


def sell(symbol, quantity=1, limit_price=0):
    f = open('History', 'a+')
    if limit_price == 0:
        api.submit_order(symbol, quantity, 'sell', 'limit', 'day', api.get_position(symbol).current_price)
    else:
        api.submit_order(symbol, quantity, 'sell', 'limit', 'day', limit_price)
    f.write('\nselling: ' + symbol + ' at ' + ' quantity: ' + str(quantity))


def main(symbol):
    trade_or_not = macd(symbol)
    if trade_or_not == 'sell':
        sell(symbol, api.get_position(symbol).qty)
        print(trade_or_not)
    if trade_or_not == 'buy':
        print('buy')
        buy(symbol, float(api.get_account().buying_power) // api.get_barset('AMD', 'day', limit=1)['AMD'][0].c)
        print(trade_or_not)
