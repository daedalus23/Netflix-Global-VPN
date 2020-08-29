from .Database import add_to_db
from .Database.db import session
from .Database.model import Movie
from .fetch import Fetch
from .apiParser import Parser
import os


def update_db():
    """Update movie dB"""

    movieSearchUrl = "https://unogsng.p.rapidapi.com/search"
    countryListUrl = "https://unogsng.p.rapidapi.com/countries"
    apiKey = os.environ.get("RAPID_KEY")

    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }

    f = Fetch(movieSearchUrl, countryListUrl, headers)

    f.get_countries()
    f.jsonResponse = Parser.convert_json_dict(f.countryResponse.text)
    f.countryList = Parser.string_creation(f.jsonResponse)

    queryString = Parser.form_query_dict(f.countryList)
    f.get_movies(queryString)
    movies = Parser.convert_json_dict(f.movieResponse.text)

    for i in range(movies["total"]):

        queryString["offset"] = i * 100

        f.get_movies(queryString)
        movies = Parser.convert_json_dict(f.movieResponse.text)

        try:
            for item in movies["results"]:
                add_to_db(
                    item["vtype"],
                    item["title"],
                    item["year"],
                    item["sysnopsis"],
                    item["runtime"],
                    item["titledate"],
                    item["clist"],
                    item["imdbid"],
                    item["avgrating"],
                    item["imdbrating"],
                    item["top250tv"],
                    item["top250"],
                    item["img"],
                    item["poster"]
                )

        except KeyError:
            pass


def query_db(searchValue=None):
    """Query movie dB"""

    temp = []

    if searchValue is None:
        for row in session.query(Movie) \
                .order_by(Movie.title) \
                .all():
            temp.append(row)
        return temp

    else:
        for row in session.query(Movie) \
                .order_by(Movie.title) \
                .filter(Movie.title.contains(searchValue.lower())):
            temp.append(row)
        return temp


__all__ = ["update_db", "query_db"]
