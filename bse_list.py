#!/usr/bin/env python
import requests as req
from bs4 import BeautifulSoup as BS
import pandas as pd

url = 'https://economictimes.indiatimes.com/indices/sensex_30_companies'

resp = req.get(url)

soup = BS(resp.text, 'html.parser')
selector = '.dataList'
stock_soups = soup.select(selector)

stock_data = []

for i in range(30):
    stock = stock_soups[i].select('li')
    name = stock[0].select_one('p').text
    ltp = stock[1].text
    change = stock[2].text
    percentage_change = stock[3].text
    volume = stock[5].text
    turnover = stock[6].text
    stock_data.append((name, ltp, change, percentage_change, volume, turnover))

df = pd.DataFrame(stock_data, columns=['name', 'last trade price', 'change', 'percecntage change', 'volume', 'turnover'])
df.to_csv('stocks.csv', index=False)

