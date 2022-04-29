from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Different kind of permissions that you can specify on API endpoint
# AllowAny = you not need to be authenticated
# IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadyOnly

from .serializers import PostSerializer
from .models import Post


# Create your views here.

# An API view is something that we can inherit in our own classes 

class TestView(APIView):
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
        return Response(serializer.errors)

# def test_view(request): # That is a dictionary then is converted in a Json payload
#    data = {
#        'name': 'john',
#        'age': 23
#    }
#    return JsonResponse(data)

    # By default the JSON response only returns a dictionary, but
    # you can pass a list using the safe argument, likes "safe=False"
    # That allows you to return a list.
    # return JsonResponse(data)