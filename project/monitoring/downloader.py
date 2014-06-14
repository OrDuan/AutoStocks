# -*- coding: utf-8 -*-
import json
import threading
from time import sleep
import urllib2
from datetime import datetime, timedelta
from project.models.db_helper import save
from project.models.portfolio import Portfolio
from project.models.stock import Stock


class DataDownloader(threading.Thread):
    def __init__(self, symbol):
        threading.Thread.__init__(self)
        self.symbol = symbol
        self.prefix = "http://finance.google.com/finance/info?client=ig&q=NASDAQ"

    def run(self):
        last_updated = datetime.now() - timedelta(hours=7)
        while True:
            url = self.prefix + ":%s" % self.symbol
            u = urllib2.urlopen(url)
            content = u.read()

            obj = json.loads(content[3:])
            date = datetime.strptime(obj[0]["lt_dts"], '%Y-%m-%dT%H:%M:%SZ')
            if date > last_updated:
                s = Stock(str(obj[0]))
                save(s)
                last_updated = date
                print "Saved: " + str(s)
            print ".",
            sleep(2)


# RUN
google_theard = DataDownloader("GOOG")
google_theard.start()

