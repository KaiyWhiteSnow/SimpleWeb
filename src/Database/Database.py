from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.state import InstanceState
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///DataBase.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

Base.metadata.create_all(engine)