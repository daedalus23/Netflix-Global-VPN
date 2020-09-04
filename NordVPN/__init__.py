from Moviedb import query_db
from WebDriver import Driver

import os
import time

driverPath = r"C:\Users\james\PycharmProjects\Netflix-Global-VPN\WebDriver\chromedriver.exe"


def main():
    os.chdir(r"C:\Program Files\NordVPN")
    url = "https://www.netflix.com/"

    entry = input("Enter in Movie: ")
    while True:
        if entry == "":
            entry = input("Please enter in Movie:")
        else:
            break

    posts = query_db(entry)

    movieList = {}
    for i, post in enumerate(posts):
        print(f"""  {i}:
                        {post.title.capitalize()},
                        {post.year},
                        {post.runtime},
                        {post.sysnopsis}\n""")

        movieList[str(i)] = post.imdbid

    selectedTitle = input("Enter number of movie: ")

    while True:
        if selectedTitle == "":
            selectedTitle = input("Please enter number of movie: ")
        else:
            break

    for post in posts:
        if movieList[selectedTitle] == post.imdbid:
            selectedMovie = post

    country = [i for i in selectedMovie.countryList.split('"') if i.__len__() > 2]
    print(country)

    os.chdir(r"C:\Program Files\NordVPN")
    os.system(f'cmd /c "nordvpn -c -g {country[0]}')
    time.sleep(2)   # seconds

    driver = Driver(driverPath)
    driver.get(url)
    driver.open_cookie()
    driver.refresh_page()

    profile = '#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > div > ul > li:nth-child(1) > div > a'
    searchBar = '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button'
    searchInput = '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/input'
    searchedMovie = '//*[@id="title-card-0-0"]/div[1]/a/div[1]/img'

    driver.click_css(profile)
    driver.click(searchBar)
    driver.input_value(searchInput, selectedMovie.title)
    driver.click(searchedMovie)


if __name__ == "__main__":
    main()
