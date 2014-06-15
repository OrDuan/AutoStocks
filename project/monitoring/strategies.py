import time
from project.models.db_helper import save
from project.models.functions import get_data_listed
from project.models.portfolio import Portfolio
from project.models.stock import Stock


class BaseStrategy():
    def __init__(self, symbol):
        self.symbol = symbol



class StrategyOne():
    """
    A basic strategy just to test the app.
    """

    def __init__(self, symbol):
        self.symbol = symbol
        self.stocks = Stock.query.filter_by(symbol=self.symbol).all()
        self.portfolio = Portfolio.query.filter_by(id=2).first()  # TODO: should be different query/input

        # Global vars
        self.last_price = 0
        self.times = 0


    def buy_when(self, stock):
        """
        [HERE GOES THE MAGIC] - we tells the strategy WHEN to buy
        Let buy a stock when its raised more then 2 time in a row.
        if it's raised more then 2 - buy the amount of times it raised
        """
        if stock.price > self.last_price:
            self.times += 1
            self.last_price = stock.price
        else:
            self.times = 0
            self.last_price = 0

        if self.times == 2:
            self.buy_stock(stock)

    def sell_when(self, stock):
        """
        [HERE GOES THE MAGIC]
        """
        pass

    def buy_stock(self, stock):
        if self.portfolio.money < stock.price:  # TODO: This if should be check when calling the strategy, not here
            print "CANT BUY - YOU DON'T HAVE MONEY"
            return False

        # Update money
        self.portfolio.money = self.portfolio.money - stock.price
        save(self.portfolio)

        # Update portfolio
        stock.portfolio = self.portfolio.id
        save(stock)
        print "Bought " + str(stock.symbol) + ": " + str(stock.price) + ", Money left: " + str(self.portfolio.money )

    def run(self):
        for stock in self.stocks:
            self.buy_when(stock)
            self.sell_when(stock)
            print "next", stock.price
            time.sleep(1)  # stimulate real-time running

    def get_stock_from_date(self, date):
        new_list = []
        for s in reversed(self.stocks):
            if s.date < date:
                new_list.append(s)
            else:
                break
        return new_list


a = StrategyOne("GOOG")
a.run()

