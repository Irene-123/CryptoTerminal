#!/usr/bin/env python3

import json
import sys 
from datetime import datetime
import requests 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



currencies =["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP",
              "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK",
              "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD",
              "USD", "ZAR"]

def get_response(top, convert):
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    if convert in currencies:
            parameters = {
            'start':'1',
            'limit':top,
            'convert':convert
            }
            headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '57da6090-2155-48f2-9b83-a362e73e1611',
            }

            session = Session()
            session.headers.update(headers)

            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.content)
                date = datetime.now().time()
                print(f'Fetched data from CoinMarketAPI at {date}')
                return data
    
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                return e

