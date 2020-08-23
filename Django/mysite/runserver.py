#!/usr/bin/env python
import os
from mysite.settings import ALLOWED_HOSTS


def main():

    url = ALLOWED_HOSTS[0]
    port = "8000"

    os.system(f'cmd /c "python manage.py runserver {url}:{port}"')


if __name__ == "__main__":
    main()
