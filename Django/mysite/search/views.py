from django.shortcuts import render
from django.core.paginator import Paginator
from .Moviedb import query_db


def home(request):

    contentList = {
        'title': 'Home',
        'posts': query_db()
    }

    # paginator = Paginator(contentList["posts"], 25)
    #
    # try:
    #     page = int(request.GET.get("page", 1))
    # except:
    #     page = 1
    #
    # try:
    #     content = paginator.page(page)
    # except:
    #     content = paginator.page(paginator.num_pages)

    return render(request, 'search/home.html', contentList)


def about(request):
    return render(request, 'search/about.html', {'title': 'About'})
