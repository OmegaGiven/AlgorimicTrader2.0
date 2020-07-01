
import alpaca_trade_api as tradeapi

f = open('API.txt', 'r')
if f.mode == 'r':
    file = f.read().split('\n')
f.close()
api = tradeapi.REST(file[0], file[1], file[2])


print(api.get_account())
# print(api.)