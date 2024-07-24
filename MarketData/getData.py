import yfinance as yf
import pandas as pd
import datetime

class MarketData:
    def __init__(self, ticker, period=720, interval="1h"):
        self._ticker = ticker
        stock = yf.Ticker(ticker)
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=720)
        end_date = end_date - datetime.timedelta(days=0)
        self._df = stock.history(start=start_date, end=end_date, interval='1h')

    def get_prices(self):
        open_prices = self._df['Open']
        return open_prices.tolist()