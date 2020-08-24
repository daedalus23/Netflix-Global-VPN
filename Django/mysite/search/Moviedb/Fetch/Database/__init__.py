"""!!!!!Credit Leftier!!!!!"""  # fancy-up

from .model import Movie
from .db import run
from .db import engine
from .db import create


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
                  title=title,
                  year=year,
                  sysnopsis=sysnopsis,
                  runtime=runtime,
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


__all__ = ["add_to_db"]
