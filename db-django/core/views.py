from django.shortcuts import render, HttpResponse

# Create your views here.

def hello (request, name, years) :
    return HttpResponse('<h1> Hello World!!</h1> <br> '
                        '<h2> Student: {}, {} years old.</h2>'.format(name, years))