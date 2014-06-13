import json
import threading
from time import sleep
import urllib2
from project.models.db_helper import save
from project.models.stock import Stock


class DataDownloader(threading.Thread):
    def __init__(self, symbol):
        threading.Thread.__init__(self)
        self.symbol = symbol
        self.prefix = "http://finance.google.com/finance/info?client=ig&q=NASDAQ"
        self.stock = Stock.query.filter_by(symbol=self.symbol).first()

    def run(self):
        while True:
            url = self.prefix + ":%s" % self.symbol
            u = urllib2.urlopen(url)
            content = u.read()

            obj = json.loads(content[3:])

            s = Stock(str(obj[0]), self.symbol)
            save(s)
            print "saved: " + str(s)
            sleep(3)

google_theard = DataDownloader("GOOG")
google_theard.start()

