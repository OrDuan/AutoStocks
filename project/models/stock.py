# -*- coding: utf-8 -*-
import ast
from datetime import datetime
from sqlalchemy import ForeignKey
from project import db


class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    symbol = db.Column(db.String(10))
    date = db.Column(db.DateTime)
    price = db.Column(db.Float)
    change = db.Column(db.Float)
    change_p = db.Column(db.Float)
    open = db.Column(db.Float)

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
