"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# obtain_auth_token is the view that will return the token for a user
# when we send the username and password so basically like a login view

from core.views import PostView, PostCreateView, TestView, PostListCreateView # test_view

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='second'), # we have to say as view because it's a class space
    path('create/', PostCreateView.as_view(), name='third'), # we have to say as view because it's a class space
    path('test/', TestView.as_view(), name='first'), 
    path('list/',PostListCreateView.as_view(), name='fourth'),
    path('api/token', obtain_auth_token, name='obtain-token') # returns the token if the username and password are correct
]
