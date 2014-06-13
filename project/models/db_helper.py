__author__ = 'Or Duan'
from project import db


def save(obj):
    session = db.session
    session.add(obj)
    session.commit()


def delete(obj):
    session = db.session
    session.delete(obj)
    session.commit()