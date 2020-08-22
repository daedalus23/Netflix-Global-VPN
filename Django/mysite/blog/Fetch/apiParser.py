import json

class Parser:

    def convert_json_dict(self):
        """convert json to dict"""
        return json.loads(self)

    def string_creation(self):
        """iterate through json to create string with ',' """

        countries = ""

        for i, country in enumerate(self["results"]):
            if i == 0:
                countries += str(country["id"])
            else:
                countries = countries + "," + str(country["id"])

        return countries

    def form_query_dict(self):
        """create new query form"""
        querystring = {"start_year": "1900",
                       "orderby": "rating",
                       "audiosubtitle_andor": "and",
                       "limit": "100",
                       "subtitle": "",
                       "countrylist": self,
                       "audio": "",
                       "country_andorunique": "",
                       "offset": "0",
                       "end_year": "2020"}

        return querystring

__all__=["Parser"]
