from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins

# Different kind of permissions that you can specify on API endpoint
# AllowAny = you not need to be authenticated
# IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadyOnly

from .serializers import PostSerializer
from .models import Post
from core import serializers


# Create your views here.

# An API view is something that we can inherit in our own classes 

class TestView(APIView):
    # permition_classes is a property we get acess to when we inherit from APIView and other rappers
    # Is authenticated means no matter wich method were sending as a request method so
    # wether it's get or post we will be authenticate in order for this view, otherwise we'll just
    # get an authenticated error.
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        # Return a list of the posts
        # Using a serializer when we retrieved a data
        qs = Post.objects.all()
        # post =  qs.first() # returning the first instance in the database
        serializer = PostSerializer(qs, many=True) # returning many instances (list of dictionaries)
        # serializer = PostSerializer(post) # returning one instance (a dictionary)
        return Response(serializer.data)

    # Using a serializer when we received a data

    # In post we make sure that data we're receiving 
    # is valid especially when we want to manipulate the database

    def post(self, request, *args, **kwargs): 
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() # save a instance of a model
            return Response(serializer.data)
        return Response(serializer.errors) 

# Mixins 
# They are basically containers of functionality that you can include in your classes
# to inherit off of that provide some sort of functionality. Always include them at the beggining of
# our inheritance in the class

# ListModeLMixin allow you to list a query set

class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    # Define some properties are required to make this work
    # first serializing the class (you can also use the method get_serializer_class)
    serializer_class = PostSerializer
    # Give a query set 
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    # Override the post method calling the create method inherited of mixins
    # That allow u to fill a form in the rest framework UI and u can post then it will create an instance
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # send an email
        serializer.save()
        #return super().perform_create(serializer)
    
# Does the same thing of the PostView class
# But u dont need to especify methods cuz them are inherited from CreteAPIView that's inheriting of GenericAPIView
# Otherwise this class dont handles the get method, for use it u can inherit ListModelMixin and override it

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

# Exactly same functionality as the previous ones
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()



""" class TestView(APIView):
    # permition_classes is a property we get acess to when we inherit from APIView and other rappers
    # Is authenticated means no matter wich method were sending as a request method method so
    # wether it's get or post we will be authenticate in order for this view, otherwise we'll just
    # get an authenticated error.
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        #data = {
        #    'name': 'john',
        #    'age': 23
        #}
        # Return a list of the posts
        # Using a serializer when we retrieved a data
        qs = Post.objects.all()
        post =  qs.first() # returning the first instance in the database
        # serializer = PostSerializer(qs, many=True) # returning many instances (list of dictionaries)
        serializer = PostSerializer(post) # returning one instance (a dictionary)
        return Response(serializer.data)

    # Using a serializer when we received a data

    # In post we make sure that data we're receiving 
    # is valid especially when we want to manipulate the database

    def post(self, request, *args, **kwargs): 
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() # save a instance of a model
            return Response(serializer.data)
        return Response(serializer.errors) """

def test_view(request): # That is a dictionary then is converted in a Json payload
    data = {
        'name': 'john',
        'age': 23
    }
    return JsonResponse(data)

    # By default the JSON response only returns a dictionary, but
    # you can pass a list using the safe argument, likes "safe=False"
    # That allows you to return a list.
    # return JsonResponse(data)