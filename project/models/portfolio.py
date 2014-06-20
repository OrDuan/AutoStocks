# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from project import Base
from project.models.db_helper import save
import user


class Portfolio(Base):
    """
    Portfolio represent a list of stocks that bought.
    each user can have more then one portfolio.
    """
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"))
    stock = relationship("Stock", backref="portfolio.id")
    quantity = Column(Integer)

    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return "< Portfolio: " + str(self.money) + " Stocks: " + str(self.stocks) + " >"