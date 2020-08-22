from .MovieDatebase import add_to_db
from .fetch import Fetch
from .apiParser import Parser
from .MovieDatebase.db import engine
from sqlalchemy.orm.query import Query
from datetime import timedelta
import os


def update_datebase():

    movieSearchUrl = "https://unogsng.p.rapidapi.com/search"
    countryListUrl = "https://unogsng.p.rapidapi.com/countries"

    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get("RAPID_KEY")
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
                add_to_db(item["vtype"],
                          item["title"],
                          item["year"],
                          item["synopsis"],
                          _convert_seconds(item["runtime"]),    #convert HH:MM:SS
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

        print("item added") #debugger: confirm item added

        if "99" in str(i):  #debugger: confirm each page commited
            print("content added to dB")


def query_database():

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
        result = connection.execute(f"select {columns} from movie")

        for item in result:
            temp.append(item)

    return temp

def _convert_seconds(item):
    """convert seconds to HH:MM:SS format"""
    try:
        return timedelta(seconds=item)

    except TypeError:
        return None

__all__=["update_datebase", "query_database"]