from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.

def say_hello(request):
    return HttpResponse('Hello world')


def homepage(request):
    return HttpResponse('Cock!! Sucker!!!')


def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menuitems(request,dish):
    items = {
        'Pasta':'Pasta bologanes',
        'Mexican':' Foodies',
        'furious':'Pete',
    }
    description = items[dish]

    return HttpResponse(f"<h2>{dish}</h2>"+ description)