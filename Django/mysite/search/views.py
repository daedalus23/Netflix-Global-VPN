from django.shortcuts import render
from Django.mysite.search.Moviedb import query_db


def home(request):
    temp = query_db()

    context = {
        'title': 'Home',
        'posts': query_db()
    }
    return render(request, 'search/home.html', context)


def about(request):
    return render(request, 'search/about.html', {'title': 'About'})
