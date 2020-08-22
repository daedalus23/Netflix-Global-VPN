from pprint import pprint
import HTML
import WebDriver
import re
import MovieDatebase as add_db


# def Search(title):
#     """Title search global Netfilx"""
#
#     firePath = r"C:\Users\james\PycharmProjects\Netflix\WebDriver\geckodriver.exe"
#
#     netflixGlobal = "https://unogs.com/"
#     searchBar = '//*[@id="navbar"]/form/div/input'
#
#     driver = WebDriver.Driver(firePath)
#     driver.get(netflixGlobal)
#     driver.inputValue(searchBar, title)
#     html = driver.page_source()
#     driver.quit()
#
#     return html


def main():
    # add_db.add_to_db(
    #     "jaws",
    #     1980,
    #     "its about a big shark",
    #     "1h:37m:17s",
    #     "canada"
    # )

    # title = "jaws"

    countryRegex = re.compile(r'title="(\w+)"')
    yearRegex = re.compile(r'movie,(.+)\)')

    hp = HTML.HtmlParser(Search("a"))

    tag_list = hp.html.find_all("div", {"class": "videodiv"})

    raw_movie_list = [tag.text for tag in tag_list if tag.span]
    raw_temp = [item.split("\n") for item in raw_movie_list]
    movie_list = [[i for i in j if i != ''] for j in raw_temp]
    yearRelease = [[yearRegex.search(i).group(1) for i in line if yearRegex.search(i) is not None] for line in
                   movie_list]

    rawCountries = hp.css_select(".listdiv .videodiv .sclist")
    countryTags = [countryRegex.search(str(tag)).group(1) for tag in rawCountries]

    print()


if __name__ == "__main__":
    main()
