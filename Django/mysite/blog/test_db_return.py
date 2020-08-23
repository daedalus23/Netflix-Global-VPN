from .Fetch import query_database
from datetime import timedelta as convert_seconds

content = query_database()

for i in range(10):
    print(content[i].title, "\n", content[i].year, "\n", content[i].sysnopsis,
          "\n", str(convert_seconds(content[i].runtime)), "\n", content[i].imdbRating, "\n\n")