# -*- coding: utf-8 -*-
from project import db
from project.models.db_helper import save


class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.Float)
    #stocks = db.relationship("Stock", backref=db.backref("portfolio.id"))

    def __repr__(self):
        return "< Portfolio: " + self.money + " Stocks: " + self.stocks + " >"


def get_money():
    return Portfolio.query.first().money


def set_money(money):
    new_money = Portfolio.query().first()
    new_money.money = money
    save(new_money)