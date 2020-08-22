#!/usr/bin/env python
import os

def main():
    os.system('cmd /c "python manage.py runserver 127.0.0.1:8000"')

if __name__=="__main__":
    main()