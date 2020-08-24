from .Database import add_to_db
from .Database.db import engine
from .fetch import Fetch
from .apiParser import Parser
import os


def update_db():
    movieSearchUrl = "https://unogsng.p.rapidapi.com/search"
    countryListUrl = "https://unogsng.p.rapidapi.com/countries"
    apiKey = os.environ.get("RAPID_KEY")

    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }

    fetch = Fetch(movieSearchUrl, countryListUrl, headers)

    fetch.get_countries()
    fetch.json_reponse = Parser.convert_json_dict(fetch.countryResponse.text)
    fetch.countryList = Parser.string_creation(fetch.json_reponse)

    queryString = Parser.form_query_dict(fetch.countryList)
    fetch.get_movies(queryString)
    movies = Parser.convert_json_dict(fetch.movieResponse.text)

    for i in range(movies["total"]):

        queryString["offset"] = i * 100

        fetch.get_movies(queryString)
        movies = Parser.convert_json_dict(fetch.movieResponse.text)

        try:
            for item in movies["results"]:
                add_to_db(
                    item["vtype"],
                    item["title"],
                    item["year"],
                    item["synopsis"],
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


def query_db():
    temp = []

    columns = """vtype, 
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
                poster"""

    with engine.connect() as connection:
        result = connection.execute(
            f"""SELECT {columns} 
                FROM movie 
                ORDER BY title"""
        )

        for item in result:
            temp.append(item)

    return temp


__all__ = ["update_db", "query_db"]
