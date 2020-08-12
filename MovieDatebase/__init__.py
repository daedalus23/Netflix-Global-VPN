"""!!!!!Credit Leftier!!!!!"""  #fancy-up

from .model import Movie
from .db import run

def add_to_db(title, year, sysnopsis, runtime, country):

    movie = Movie(
                title=title,
                year=year,
                sysnopsis=sysnopsis,
                runtime=runtime,
                country=country
    )

    run(movie)

__all__ = ["add_to_db"]s