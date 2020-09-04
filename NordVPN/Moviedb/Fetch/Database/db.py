"""!!!!!Credit Leftier!!!!!"""  # fancy-up

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

dbPath = "sqlite:///C:\\Users\\james\\PycharmProjects\\Netflix-Global-VPN\\Django\\mysite\\search\\Moviedb\\Moviedb.db"

engine = create_engine(dbPath)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def run(Movie):
    """Add movie to db, catch duplicates and rollback session"""
    session.add(Movie)

    try:
        session.commit()

    except:
        session.rollback()


def create(engine):
    """Create new dB"""
    Base.metadata.create_all(bind=engine)
