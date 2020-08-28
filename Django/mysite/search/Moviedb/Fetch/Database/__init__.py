"""!!!!!Credit Leftier!!!!!"""  # fancy-up

from .model import Movie
from .db import run
from .db import engine
from .db import create
from datetime import timedelta


def add_to_db(vtype=None,
              title=None,
              year=None,
              sysnopsis=None,
              runtime=None,
              titledate=None,
              countryList=None,
              imdbid=None,
              avgrating=None,
              imdbRating=None,
              top250tv=None,
              top250=None,
              img=None,
              poster=None
              ):

    movie = Movie(vtype=vtype,
                  title=title.lower(),
                  year=year,
                  sysnopsis=sysnopsis,
                  runtime=convert_time(runtime),
                  titledate=titledate,
                  countryList=countryList,
                  imdbid=imdbid,
                  avgrating=avgrating,
                  imdbRating=imdbRating,
                  top250tv=top250tv,
                  top250=top250,
                  img=img,
                  poster=poster
                  )

    create(engine)
    run(movie)


def convert_time(seconds=None):
    """Convert seconds into HH:MM:SS"""
    try:
        convertedTime = timedelta(seconds=seconds)
        return str(convertedTime)
    except TypeError:
        return "0"


__all__ = ["add_to_db"]
