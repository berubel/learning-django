# Mapping URLs to views

from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    # path('playground/hello', views.say_hello) -> No longer need add playground here, 
    path('hello/', views.say_hello)             # because it was add in the main url conf module
]