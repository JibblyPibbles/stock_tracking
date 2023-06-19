import requests
import pprint
import pandas as pd
import re
from pathlib import Path

AV_API_KEY = 'YOUR_API_KEY'
AV_URL = 'https://www.alphavantage.co/query'
SHEETY_ENDPOINT = 'https://api.sheety.co/e66ef7bc0eab43af993d426d75098c04/stocksTracker/myStocks'

pp = pprint.PrettyPrinter(indent=4)
regex = re.compile('[^a-zA-Z]')

tsd_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'BLK',
    'outputsize': 'compact',
    'apikey':AV_API_KEY,
}

symbol_search_params = {
    'function': 'SYMBOL_SEARCH',
    'keywords': 'blackrock',
    'datatype': 'json',
    'apikey': AV_API_KEY
}

global_quote_params = {
    'function': 'GLOBAL_QUOTE',
    'symbol': 'BLK',
    'apikey': AV_API_KEY
}

# r = requests.get(AV_URL, params=global_quote_params)

# data = r.json()
# pp.pprint(data)
# print(data)

stock_tickers = ['BLK', 'GOLD', 'BDRY', 'GS', 'JPM']
stock_dicts = [{'Global Quote': {'01. symbol': 'BLK', '02. open': '715.4500', '03. high': '716.3550', '04. low': '702.3500', '05. price': '702.7800', '06. volume': '1281867', '07. latest trading day': '2023-06-16', '08. previous close': '711.1900', '09. change': '-8.4100', '10. change percent': '-1.1825%'}}, {'Global Quote': {'01. symbol': 'GOLD', '02. open': '16.6300', '03. high': '16.7900', '04. low': '16.4850', '05. price': '16.7100', '06. volume': '21152067', '07. latest trading day': '2023-06-16', '08. previous close': '16.4900', '09. change': '0.2200', '10. change percent': '1.3341%'}}, {'Global Quote': {'01. symbol': 'BDRY', '02. open': '6.1700', '03. high': '6.1700', '04. low': '6.0500', '05. price': '6.1400', '06. volume': '408732', '07. latest trading day': '2023-06-16', '08. previous close': '6.3400', '09. change': '-0.2000', '10. change percent': '-3.1546%'}}, {'Global Quote': {'01. symbol': 'GS', '02. open': '341.3800', '03. high': '341.4000', '04. low': '337.1101', '05. price': '338.3100', '06. volume': '4544941', '07. latest trading day': '2023-06-16', '08. previous close': '339.7400', '09. change': '-1.4300', '10. change percent': '-0.4209%'}}, {'Global Quote': {'01. symbol': 'JPM', '02. open': '143.0500', '03. high': '143.9650', '04. low': '142.5000', '05. price': '143.2600', '06. volume': '13813512', '07. latest trading day': '2023-06-16', '08. previous close': '143.0900', '09. change': '0.1700', '10. change percent': '0.1188%'}}]
my_stocks = [s['Global Quote'] for s in stock_dicts]

for t in range(len(stock_tickers)):
    new_param = {
    'function': 'GLOBAL_QUOTE',
    'symbol': stock_tickers[t],
    'apikey': AV_API_KEY
}
    new_request = requests.get(AV_URL, params=new_param)
    stock_dicts.append(new_request.json())

# print(stock_dicts)

my_data = {'Global Quote': {'01. symbol': 'BLK', '02. open': '715.4500', '03. high': '716.3550', '04. low': '702.3500', '05. price': '702.7800', '06. volume': '1281867', '07. latest trading day': '2023-06-16', '08. previous close': '711.1900', '09. change': '-8.4100', '10. change percent': '-1.1825%'}}
x = [my_data['Global Quote']]

my_keys = []
for s in my_stocks:
    my_keys.append(s.keys())

print(my_keys)
# keys = my_data['Global Quote'].keys()
new_keys = []
count = 0

for i in my_keys[count]:
    new_i = regex.sub('', i)
    new_keys.append(new_i)
    count += 1

print(new_keys)
final_list = []
for m in range(len(my_stocks)):
    final_dict = dict(zip(new_keys, list(my_stocks[m].values())))
    final_list.append(final_dict)

print(final_list)
df = pd.DataFrame(final_list)
#check if file exists
my_file = Path('my_stocks.csv')
if my_file.is_file():

    df.to_csv('my_stocks.csv', mode='a', index=False, header=False)
    print("data appended successfully")
else:
    df.to_csv('my_stocks.csv', index=False, header=True)

