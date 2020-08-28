from Moviedb import query_db
from Moviedb import update_db
from pprint import pprint


def main():
    """update Movie database"""
    # update_db()
    posts = query_db("rick")

    for post in posts:
        print(f"""{post.title.capitalize()},
                    {post.runtime},
                    {post.year}""")


if __name__ == "__main__":
    main()
