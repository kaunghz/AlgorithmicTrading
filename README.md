After interning at a quant trading company, I became curious about US market stocks and how to profit from them. So, I started learning about personal finance and investing. Recently, I wrote an article about why you should invest [here](https://khznote.notion.site/Invest-early-the-power-of-compound-interest-3b5a087607c2416fadf653e370ad3223)
With some computer science background, I created an algorithmic trading strategies repo where I develop and backtest using data from the past 2 years (720 days to be exact).

As of now, I developed an algorithm based off of one of the simple algorithmic trading strategies, [Trailing Stop-Loss](https://www.investopedia.com/articles/trading/08/trailing-stop-loss.asp). The basic outline of my algorithm follows:
```
        Algorithm summary
        -----------------
    keep track of the minimum price
    if the current price hits 120% of the minimum price, the stock keeps likely going up --> BUY
    For BUY, set the initial low and high bar to sell (managing the risk)

    After BUY, we either HOLD them or SELL them
    if the price keeps going up, we keep updating the low and high bar
    if the price hits either low or high bar, we sell them
```
The details can be found in Strategy/trailingStop.py. Then, I backtested with the data from 720 days before.

For back testing, I tested with the list of diversed US stocks, most volatile stocks, big tech stocks. This strategy OUTPERFORMED everything compared to you just hold them for 2 years. This strategy is even more visible in fluctuating and volatile market like TESLA. Some backtest results are:
```
Backtest on most volatile stocks including 'TSLA', 'OVV', 'OPEN', 'QS', 'MP', 'NIO', 'HRI', 'RUN', 'COIN', 'PLTR', 'CLF', 'SHOP'
----------Summary----------
Original balance $100000.00
Total TS amount $128809.16 - Total TS profit percent 28.81%
Total HOLD amount $106521.39 - Total HOLD profit percent 6.52%
```
```
Backtest with Big tech stocks 'AAPL', 'MSFT', 'GOOGL', 'NVDA', 'NFLX', 'QQQ', 'SPY', 'TSLA'
----------Summary----------
Original balance $100000.00
Total TS amount $269225.14 - Total TS profit percent 169.23%
Total HOLD amount $217763.78 - Total HOLD profit percent 117.76%
```
