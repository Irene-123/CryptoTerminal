# CryptoTerminal

### It's a python command line tool which shows you cryptocurrencies market data by using CoinMarketCap API

Fiat currencies supported: 
```
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP",
"HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK",
"NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD",
"USD", "ZAR"
```

## How to use? 

- Check the coins that you are interested in with the `-f` parameter. Use this flag with a string of separated symbols. Example use is:
```
$ python3 main.py -f "ETH, BTC, XRP, BCH"
```
- Automatically refresh the information every `rate` seconds by using the `-r` or parameter
- Display the first `top` currencies by using the `-t` parameter

```
usage: main.py [-h] [-v] [-c currency] [-f list] [-r rate] [-t top]

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  display version information and exit
  -c currency    convert to your preferred fiat currency
  -f list        only display your desired coins
  -r rate        automatically refresh information every <rate> seconds
  -t top         display the first <top> currencies
```

- Display information about the current top 10 listings by running the tool without any options. This is the default behaviour
- Terminal colours to make the displayed statistics nicer on the eyes
- Don't forget you can combine flags as you please. For example if you are interested in the top 5 coins, converted to euros and refreshed every 20 minutes, you'd do:
```
$ ./main.py -t 5 -c EUR -r 1200
```
