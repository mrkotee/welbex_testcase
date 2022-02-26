from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String)
    amount = Column(Float)  # amount in kilograms
    distance = Column(Integer)  # distance in meters

    def __init__(self, date, name, amount, distance):
        self.date = date
        self.name = name
        self.amount = amount
        self.distance = distance
