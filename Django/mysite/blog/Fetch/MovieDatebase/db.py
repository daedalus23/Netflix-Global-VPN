"""!!!!!Credit Leftier!!!!!"""  #fancy-up

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *


dbPath = "sqlite:///C:\\Users\\james\\PycharmProjects\\Netflix\\Django\\mysite\\blog\\Fetch\\MovieDatebase\\Moviedb.db"

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
    Base.metadata.create_all(engine)