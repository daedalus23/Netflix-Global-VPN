from Moviedb import query_db
from Moviedb import update_db


def main():
    """update Movie database"""
    # update_db()
    temp = query_db()

    for i in range(10):
        print(temp[i]["title"], "\n")


if __name__ == "__main__":
    main()
