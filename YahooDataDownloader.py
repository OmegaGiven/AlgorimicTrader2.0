import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests, time


def downloader(stock):
    # 31556926 is the amount of sec in a year
    url = 'https://finance.yahoo.com/v7/finance/download/' + stock + '?period1=' + "1565557243" + '&period2=' + "1597179643" +'&interval=1d&events=history'
    page = requests.get(url)

    text = BeautifulSoup(page.text, 'html.parser')
    print(text.prettify())
    for link in text.find_all("a"):
        ref = link.get('href')
        print(ref)

    r = requests.get(url, allow_redirects=True)
    open(stock + '.csv', 'wb').write(r.content)


downloader('MSFT')

"https://query1.finance.yahoo.com/v7/finance/download/AMD?period1=1565557243&period2=1597179643&interval=1d&events=history"