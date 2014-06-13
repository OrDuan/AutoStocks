from project import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(400))
    symbol = db.Column(db.String(10))

    def __init__(self, data, symbol):
        self.data = data
        self.symbol = symbol

    def __repr__(self):
        return "< Stock: " + self.symbol + " >"
