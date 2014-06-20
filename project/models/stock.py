# -*- coding: utf-8 -*-
import ast
from datetime import datetime
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Float
from project import db, Base


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10))
    portfolio = Column(Integer, ForeignKey("portfolio.id"))
    date = Column(DateTime)
    price = Column(Float)
    change = Column(Float)
    change_p = Column(Float)
    open = Column(Float)

    def __init__(self, data):
        dict_data = ast.literal_eval(data)
        self.symbol = dict_data["t"]
        self.date = str(datetime.strptime(dict_data["lt_dts"], '%Y-%m-%dT%H:%M:%SZ'))
        self.price = dict_data["l"]
        self.change = dict_data["c"]
        self.change_p = dict_data["cp"]
        self.open = dict_data["pcls_fix"]

    def __repr__(self):
        return "< Stock: " + self.symbol + " Price: " + str(self.price) + " >"
