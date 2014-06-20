import time
from project.models.db_helper import save
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
        [HERE GOES THE MAGIC] - we tells the strategy WHEN to BUY
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
        [HERE GOES THE MAGIC] - we tells the strategy WHEN to SELL
        """
        pass

    def buy_stock(self, stock):
        """
        action to commit when we want to buy
        """
        if self.portfolio.money < stock.price:  # TODO: This if should be check when calling the strategy, not here
            print "CANT BUY - YOU DON'T HAVE MONEY: " + str(stock.price)
            return False

        # Update money
        self.portfolio.money = self.portfolio.money - stock.price
        save(self.portfolio)

        # Update portfolio
        stock.portfolio = self.portfolio.id
        save(stock)
        print "Bought " + str(stock.symbol) + ": " + str(stock.price) + ", Money left: " + str(self.portfolio.money )

    def sell_stock(self):
        """
        action to commit when we want to buy
        """
        pass

    def run(self):
        for stock in self.stocks:
            print "Checking: ", stock.price
            self.buy_when(stock)
            self.sell_when(stock)
            time.sleep(1)  # stimulate real-time running

    def get_stock_from_date(self, date):
        """
        returns all the stocks from a given date.
        """
        new_list = []
        for s in reversed(self.stocks):  # iterate the stocks from the end(closer date) and return only dates who older then date
            if s.date < date:
                new_list.append(s)
                print s.date, " < ", date
        return new_list


a = StrategyOne("GOOG")
#a.run()
#print a.get_stock_from_date(datetime(2014, 6, 13, 14, 2, 50))
