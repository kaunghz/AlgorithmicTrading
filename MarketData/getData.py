import yfinance as yf
import pandas as pd
import datetime
import os

class MarketData:
    def __init__(self, ticker, period=720, interval="1h"):
        self._ticker = ticker
        stock = yf.Ticker(ticker)
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=720)
        end_date = end_date - datetime.timedelta(days=0)
        self._df = stock.history(start=start_date, end=end_date, interval='1h')
        if self._df.empty:
            try:
                self._ticker = ticker
                file_path = f'data/{self._ticker}.csv'
                stock_data = pd.read_csv(file_path)
                self._df = stock_data
            except FileNotFoundError:
                raise ValueError(f"Data not found for ticker: {self._ticker}")
        self._df.sort_index(inplace=True)
        # self.save_to_csv()

    def get_prices(self):
        open_prices = self._df['Open']
        return open_prices.tolist()

    def save_to_csv(self):
        os.makedirs("data", exist_ok=True)
        file_path = f"data/{self._ticker}.csv"
        if os.path.exists(file_path):
            try:
                existing_data = pd.read_csv(file_path, index_col=0, parse_dates=True)
            except ValueError:
                # If 'Date' is not in the CSV file, we'll assume there's no date column
                existing_data = pd.read_csv(file_path)
            updated_data = pd.concat([existing_data, self._df])
            updated_data = updated_data[~updated_data.index.duplicated(keep="last")]
            updated_data.sort_index(inplace=True)
        else:
            updated_data = self._df
        updated_data.to_csv(file_path)
        print(f"Data successfully saved to {file_path}")
