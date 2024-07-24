'''
Author - Kaung Zan
Algorithmic Trade Algorithm
'''

from BackTest.BTTrailingStop import BTTrailingStop

if __name__ == "__main__":
    tickers = [
        "AAPL",  # Apple Inc.
        "MSFT",  # Microsoft Corporation
        "AMZN",  # Amazon.com, Inc.
        "GOOGL",  # Alphabet Inc. Class A
        "META",  # Meta Platforms, Inc.
        "TSLA",  # Tesla, Inc.
        "JNJ",   # Johnson & Johnson
        "V",     # Visa Inc.
        "JPM",   # JPMorgan Chase & Co.
        "NVDA",  # NVIDIA Corporation
        "DIS",   # The Walt Disney Company
        "PYPL",  # PayPal Holdings, Inc.
        "NFLX",  # Netflix, Inc.
        "KO",    # The Coca-Cola Company
        "PEP",   # PepsiCo, Inc.
        "INTC",   # Intel Corporation
        "IBM",   # International Business Machines Corporation
        "BA",    # The Boeing Company
        "UAL",    # United Airlines Holdings, Inc.
    ]
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'NFLX', 'QQQ', 'SPY', 'TSLA']

    # some most volatile stocks from https://finance.yahoo.com/news/16-most-volatile-stocks-buy-141732618.html
    tickers = ['TSLA', 'OVV', 'OPEN', 'QS', 'MP', 'NIO', 'HRI', 'RUN', 'COIN', 'PLTR', 'CLF', 'SHOP']
    trailing_stop = BTTrailingStop(tickers)
    trailing_stop.run()