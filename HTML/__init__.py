from bs4 import BeautifulSoup
import WebDriver
import re

class HtmlParser:

    def __init__(self, html):
        self.html = BeautifulSoup(html, "html.parser")

    def regex_search(self, regex, data):
        """Regex pattern searchs List; strip None and return remaining"""

        RawList = []

        for line in data:
            RawList.append(regex.search(str(line)))

        return [x[1] for x in RawList if x is not None]

    def css_select(self, selector):
        """Return CSS selector"""
        return self.html.select(selector)
