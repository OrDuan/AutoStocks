from project import db


class Money(db.Model):
    money = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "< Money: " + self.money + " >"
