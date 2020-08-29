from Moviedb import query_db
from Moviedb import update_db
from pprint import pprint
import os


def main():
    """update Movie database"""
    # update_db()
    posts = query_db("once upon a time")

    for post in posts:
        print(f"""{post.title.capitalize()},
                    {post.runtime},
                    {post.imdbid}
                    {post.countryList},
                    {post.sysnopsis}""")

    selectedTitle = input("Enter Imdb ID:")
    selectedMovie = None

    for post in posts:
        if post.imdbid is selectedTitle:
            selectedMovie = post

    countryList = [i for i in selectedMovie.countryList('"') if len(i) > 2]
    os.system(f'cmd /c cd "C:\Program Files\NordVPN"')


if __name__ == "__main__":
    main()
