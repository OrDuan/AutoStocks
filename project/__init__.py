# -*- coding: utf-8 -*-
from flask import Flask
import flask.ext.restless
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Why would the fisherman say what the fisherman says that the fisherman says... well, i have no idea'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/stocks'

db = SQLAlchemy(app)


# Controllers
import controllers.stock

# Models
import models.stock
import models.money


