from bs4 import BeautifulSoup


class HtmlParser:

    def __init__(self, html):
        self.html = BeautifulSoup(html, "html.parser")

    @staticmethod
    def regex_search(regex, data):
        """Regex pattern searches List; strip None and return remaining"""

        RawList = []

        for line in data:
            RawList.append(regex.search(str(line)))

        return [x[1] for x in RawList if x is not None]

    def css_select(self, selector):
        """Return CSS selector"""
        return self.html.select(selector)
