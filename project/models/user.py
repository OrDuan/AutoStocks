# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship
from project import Base, db
from project.models.db_helper import save


class User(Base):
    """
    This class is temporary - it's stimulate the owner money
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    portfolio = relationship("Portfolio", backref="user.id")
    money = Column(Float)

    def __init__(self, money):
        self.money = money

    def __repr__(self):
        return "<User: " + str(self.id) + ">"

def get_money():
    return db.query(User).first().money


def set_money(money):
    new_money = db.query(User).first()
    new_money.money = money
    save(new_money)