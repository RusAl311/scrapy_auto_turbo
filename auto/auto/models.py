from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class Auto(Base):
    __tablename__ = "Autos"

    id = Column(Integer, primary_key=True)
    city = Column('City', String)
    brand = Column('Brand', String)
    model = Column('Model', String)
    year = Column('Year', Integer)
    bodytype = Column('BodyType', String)
    color = Column('Color', String)
    engine = Column('Engine', Float)
    power = Column('Power', Integer)
    fuel = Column('Fuel', String)
    mileage = Column('Mileage', Integer)
    transmission = Column('Transmission', String)
    drivetype = Column('DriveType', String)
    new = Column('New', Boolean)
    pricem = Column('PriceM', Integer)
    priced = Column('PriceD', Integer)
    order = Column('Order', Integer, nullable=False)
    name = Column('Name', String)
    number = Column('Number', String)
    adddate = Column('AddDate', Date)

class SalonAuto(Base):
    __tablename__ = "SalonAutos"

    id = Column(Integer, primary_key=True)
    city = Column('City', String)
    brand = Column('Brand', String)
    model = Column('Model', String)
    year = Column('Year', Integer)
    bodytype = Column('BodyType', String)
    color = Column('Color', String)
    engine = Column('Engine', Float)
    power = Column('Power', Integer)
    fuel = Column('Fuel', String)
    mileage = Column('Mileage', Integer)
    transmission = Column('Transmission', String)
    drivetype = Column('DriveType', String)
    new = Column('New', Boolean)
    pricem = Column('PriceM', Integer)
    priced = Column('PriceD', Integer)
    order = Column('Order', Integer)