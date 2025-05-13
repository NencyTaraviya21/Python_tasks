from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base_url = "sqlite:///database.db"
engine = create_engine(base_url)

Base = declarative_base()

# to create table and columns
class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)  # declare datatype and set pk true if required
    name = Column(String)

Base.metadata.create_all(engine)  # this creates all the tables and data related to it
