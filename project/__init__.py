# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql://root:@localhost/autostocks')

Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()


# Controllers
import controllers.stock

# Models
import models.stock
import models.portfolio


