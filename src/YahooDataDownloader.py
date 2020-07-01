import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests


def downloader(stock):

    # url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock
    url = 'https://finance.yahoo.com/quote/' + stock + '/history?p='
    page = requests.get(url)
    # print(page.text.startswith('https://query1.finance.yahoo.com/v7/finance/download/'))




    text = BeautifulSoup(page.text, 'html.parser')
    print(text.prettify())
    for link in text.find_all("a"):
        ref = link.get('href')
        print(ref)



    # r = requests.get(url, allow_redirects=True)
    # open(stock + 'csv', 'wb').write(r.content)

downloader('MSFT')
