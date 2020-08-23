"""!!!!!Credit Leftier!!!!!"""  # fancy-up

from sqlalchemy import Column, Integer, String, FLOAT, DateTime
from .db import Base


class Movie(Base):
    __tablename__ = "movie"
    id = Column("id", Integer, primary_key=True)
    vtype = Column("vtype", String)
    title = Column("title", String, unique=True)
    year = Column("year", Integer)
    sysnopsis = Column("sysnopsis", String)
    runtime = Column("runtime", DateTime)
    titledate = Column("titledate", String)  # re-format to datetime
    countryList = Column("countryList", String)  # parsh out by "\"
    imdbid = Column("imdbid", String)
    avgrating = Column("avgrating", FLOAT)
    imdbRating = Column("imdbRating", FLOAT)
    top250tv = Column("top250tv", Integer)
    top250 = Column("top250", Integer)
    img = Column("img", String)  # Re-format to get request
    poster = Column("poster", String)

    def __init__(self,
                 vtype,
                 title,
                 year,
                 sysnopsis,
                 runtime,
                 titledate,
                 countryList,
                 imdbid,
                 avgrating,
                 imdbRating,
                 top250tv,
                 top250,
                 img,
                 poster
                 ):
        self.vtype = vtype
        self.title = title
        self.year = year
        self.sysnopsis = sysnopsis
        self.runtime = runtime
        self.titledate = titledate
        self.countryList = countryList
        self.imdbid = imdbid
        self.avgrating = avgrating
        self.imdbRating = imdbRating
        self.top250tv = top250tv
        self.top250 = top250
        self.img = img
        self.poster = poster


__all__ = ["Movie"]
