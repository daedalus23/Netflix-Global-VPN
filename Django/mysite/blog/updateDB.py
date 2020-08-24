from Moviedb import query_db
from Moviedb import update_db

def main():
    """update Movie database"""
    update_db()
    temp = query_db()

    print(temp[0]["title"])


if __name__ == "__main__":
    main()
