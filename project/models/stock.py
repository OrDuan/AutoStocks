from sqlalchemy import ForeignKey
from project import db


class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    portfolio = db.Column(db.Integer(), ForeignKey('portfolio.id'))
    symbol = db.Column(db.String(10))
    price = db.Column(db.Float)

    def __init__(self, data, symbol):
        self.symbol = symbol
        self.price = 1


    def __repr__(self):
        return "< Stock: " + self.symbol + " >"
