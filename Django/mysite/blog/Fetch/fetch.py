import requests

class Fetch:

    countryResponse = None
    movieResponse = None
    json_reponse = None
    countryList = None

    def __init__(self, movieSearchUrl, countryListUrl, header):
        self.movieSearchUrl = movieSearchUrl
        self.countryListUrl = countryListUrl
        self.header = header

    def get_movies(self, queryString):
        """get request for json movie list per country code"""
        self.movieResponse = requests.request("GET",
                                         self.movieSearchUrl,
                                         headers=self.header,
                                         params=queryString)

    def get_countries(self):
        """get request for json country list"""
        self.countryResponse = requests.request("GET",
                                         self.countryListUrl,
                                         headers=self.header)

__all__=["Fetch"]


