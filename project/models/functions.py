# -*- coding: utf-8 -*-
from project.models.user import get_money, set_money

__author__ = 'Or Duan'
import csv


def buy(stock, quantity):
    """
    Buy action:
    - Update the current money
    - Print status

    Can get a stock object or price
    """
    money = get_money()
    if type(stock) != float:
        set_money(money-(float(stock.price) * quantity))
        print "Bought " + str(quantity) + " of " + stock.symbol + " stocks for " + str(stock.price) + " each"
    else:
        set_money(money-(float(stock) * quantity))
        print "Bought " + str(quantity) + " of " + str(stock) + " each"


def sell(stock, quantity):
    """
    Sell action:
    - Update the current money
    - Print status
    """
    money = get_money()
    if type(stock) != float:
        set_money(money+(float(stock.price) * quantity))
        print "Sold " + str(quantity) + " of " + stock.symbol + " stocks for " + str(stock.price) + " each"
    else:
        set_money(money+(float(stock) * quantity))
        print "Sold " + str(quantity) + " of " + str(stock) + " each"


def get_data_listed(symbol, lineno):
    """
    returns list of lists of all the rows in the the 'symbol'.csv file
    lineno is the maximum line number to read - that will stimulate a real time data
    """
    line_counter = 0
    with open("data/" + symbol + ".csv", "r") as fp:
        a = csv.reader(fp)
        flag = False
        data_listed = []
        for i in a:
            if flag:
                if line_counter < lineno:
                    data_listed.append(i)
            else:
                flag = True
            line_counter += 1
        return data_listed