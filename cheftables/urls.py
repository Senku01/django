from django.urls import path 
from . import views

urlpatters = [
    path('/say_hello',views.say_hello),
]