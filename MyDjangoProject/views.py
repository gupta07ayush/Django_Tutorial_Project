# @gupta07ayush
# HttpResponse is used to display text data on browser which you want to show.
# render is used to render(display) html page(template) on browser as a response.
# request is used when you want to get data from a form.
# Make functions for every task then map to urls.py
# render takes two arguments, first is request and second .html templates which has to render

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # html template which will render on home page.
    return render(request, 'index.html')


def gupta(request):
    return HttpResponse("<h1><center>My name is Ayush Gupta<center></h1>")


# make function to dynamic urls to fetch and show multiple urls(blog posts). we can fetch data with the help of id from the database using where clause.
def dynamic(request, courseid):
    return HttpResponse(courseid)
