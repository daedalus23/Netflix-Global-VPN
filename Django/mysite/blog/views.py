from django.shortcuts import render
from .Fetch import update_datebase

from .Fetch import query_database

def home(request):
    context = {
        'title': 'Home',
        'posts': query_database()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})