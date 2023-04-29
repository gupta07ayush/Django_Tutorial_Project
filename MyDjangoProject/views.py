# @gupta07ayush
# HttpResponse is used to display text data on browser which you want to show.
# render is used to render(display) html page(template) on browser as a response.
# request is used when you want to get data from a form.
# Make functions for every task then map to urls.py

from django.http import HttpResponse


def gupta(request):
    return HttpResponse("<h1><center>Welcome to the world of the Guptaji.</center></h1>")


def home(request):
    return HttpResponse("<h1><center>My name is Ayush Gupta<center></h1>")


# make function to dynamic urls to fetch and show multiple urls(blog posts). we can fetch data with the help of id from the database using where clause.
def dynamic(request, courseid):
    return HttpResponse(courseid)
