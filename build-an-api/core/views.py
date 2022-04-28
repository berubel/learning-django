from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

# Create your views here.

# An API view is something that we can inherit in our own classes 

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'john',
            'age': 23
        }
        return Response(data)

    # Using a serializer when we received a data

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
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