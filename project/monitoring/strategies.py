from project.models.functions import get_data_listed


class BaseStrategy():
    def __init__(self, symbol):
        self.symbol = symbol



class StrategyOne():
    """
    Let buy a stock when its raised more then 2 time in a row.
    if it's raised more then 2 - buy the amount of times it raised
    """

    def __init__(self, stock):
        self.stock = stock
        self.data = get_data_listed(stock.symbol, 2)

    def buy_when(self):
        pass

    def sell_when(self):
        pass

