import csv


def loader(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        daily_close = []
        for row in csv_reader:
            if line_count != 0:
                daily_close.append(float(row[4]))
            line_count += 1
        # print(f'Processed {line_count} lines.')
        return daily_close


def MeanReversion(five_day, current_day):
    total = 0
    for i in five_day:
        total += float(i)
    moving_average = total / 5
    if current_day < moving_average * .97:
        return 'buy'
    else:
        return 'sell'


def margingains(moving_average, current_day):
    if current_day > moving_average * 1.2:
        return True
    else:
        return False


def calculate(filename):
    daily_close_list = loader(filename)
    # print(daily_close_list)
    x = 20
    status = 1
    account = 100
    print('start account: ' + str(account))
    buy_counter = 0
    sell_counter = 0
    while x < len(daily_close_list):
        five_day_list = [daily_close_list[x-1], daily_close_list[x-2], daily_close_list[x-3], daily_close_list[x-4], daily_close_list[x-5]]
        do_what = MeanReversion(five_day_list, daily_close_list[x])
        if do_what == 'buy' and status == 0 and account >= daily_close_list[x]:
            account = account - daily_close_list[x]
            print('buy at: ' + str(daily_close_list[x]))
            buy_counter += 1
            status = 1
        elif do_what == 'sell' and status == 1:
            account += daily_close_list[x]
            print('sell stock at: ' + str(daily_close_list[x]))
            status = 0
            sell_counter += 1
        # print(account)
        x += 1

    print('amount of buys: ' + str(buy_counter))
    print('amount of sells: ' + str(sell_counter))
    print('account at day ' + str(x) + ': ' + str(account))
    print('amount gain: ' + str(account - (100 + daily_close_list[0])))
    print('percent gain: ' + str((account - (100 + daily_close_list[0])) / daily_close_list[0] *100) + '\n\n\n')
    # print('done')

print('testing MSFT:')
calculate('testFiles/MSFT.csv')

print('testing TSLA:')
calculate('testFiles/TSLA.csv')

print('testing AMD:')
calculate('testFiles/AMD.csv')

print('testing RCL:')
calculate('testFiles/RCL.csv')
