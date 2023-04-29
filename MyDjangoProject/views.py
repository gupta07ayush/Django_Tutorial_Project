# HttpResponse is used to display text data on browser which you want to show.
# render is used to render(display) html page(template) on browser.
# request is used when you want to get data from a form.
from django.http import HttpResponse

# Make functions for every task then map to urls.py

def gupta(request):
    return HttpResponse("<h1><center>Welcome to the world of the Guptaji.</center></h1>")

def home(request):
    return HttpResponse("<h1><center>My name is Ayush Gupta<center></h1>")
