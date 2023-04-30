# @gupta07ayush
# HttpResponse is used to display text data on browser which you want to show.
# render is used to render(display) html page(template) on browser as a response.
# request is used when you want to get data from a form.
# Make functions for every task then map to urls.py
# render takes three arguments, first is request and second .html templates which has to render
# third is a dictionary which pass the data from views to html template
# we can get data here from database and send to the template.

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # use key of data in the index.html page to send the value 'Home page' in {{title}}
    data = {
        'title': 'Home Page',
        'age': 25,

    }
    # html template which will render on home page.
    return render(request, 'index.html', data)


def gupta(request):
    return HttpResponse("<h1><center>My name is Ayush Gupta<center></h1>")


# make function to dynamic urls to fetch and show multiple urls(blog posts). we can fetch data with the help of id from the database using where clause.
def dynamic(request, courseid):
    return HttpResponse(courseid)
