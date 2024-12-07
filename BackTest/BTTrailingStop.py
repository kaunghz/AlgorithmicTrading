from MarketData.getData import MarketData
from Strategy.trailingStop import trailingStop

class BTTrailingStop:
    def __init__(self, tickers, balance=10000):
        self.tickers = sorted(tickers)
        self.balance = balance

    def run(self):
        splitted_balance = self.balance / len(self.tickers)
        result = 0
        hold_result = 0
        for ticker in self.tickers:
            md = MarketData(ticker)
            prices = md.get_prices()
            back_test = trailingStop(balance=splitted_balance)
            trailingstop_amount = back_test.back_test(prices)
            print("{} - TS amount ${:.2f} - TS profit percent {:.2f}%".format(
                ticker, trailingstop_amount, self._profit_percent(splitted_balance, trailingstop_amount)))
            cur_hold = self._calculate_hold_profit(ticker, prices[0], prices[-1], splitted_balance)
            print("--------------------------------------------------------")
            result += trailingstop_amount
            hold_result += cur_hold
        self._summarize(self.balance, result, hold_result)

    def _profit_percent(self, org, after):
        return float((after - org) / org * 100)

    def _summarize(self, original, final, hold_final):
        print("----------Summary----------")
        print("Original balance ${:.2f}".format(original))
        print("Total TS amount ${:.2f} - Total TS profit percent {:.2f}%".format(
            final, self._profit_percent(original, final)))
        print("Total HOLD amount ${:.2f} - Total HOLD profit percent {:.2f}%".format(
            hold_final, self._profit_percent(original, hold_final)))
        if hold_final < final:
            print("\033[1;32mBeated Hold\033[0m")
        else:
            print("\033[1;31mLost Hold\033[0m")
        print("---------------------------")

    def _calculate_hold_profit(self, ticker, buy_price, sell_price, org_amount):
        profit = sell_price - buy_price
        stocksOwned = org_amount // buy_price
        # remaining_amount = org_amount - (stocksOwned * buy_price)
        final_amount = org_amount + (stocksOwned * profit)
        percent = self._profit_percent(org_amount, final_amount)
        print("{} - HOLD profit amount ${:.2f} - HOLD profit percent {:.2f}%".format(ticker, final_amount, percent))
        return final_amount
