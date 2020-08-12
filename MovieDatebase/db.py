"""!!!!!Credit Leftier!!!!!"""  #fancy-up

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///C:\\Users\\james\\PycharmProjects\\Netflix\\MovieDatebase\\Moviedb.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(engine)

def run(self):
    session.add(self)
    session.commit()