from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A view function takes a request and returns a response
# request -> response 
# request handler (in some framework it's call an action, in django is view)

def calculate():
    x = 1
    y = 2
    return x + y

def say_hello(request):
    # Examples in real cenary for a view function:
    # Pull data from db
    # Transform
    # Send email
    # return HttpResponse('Hello World') -> returns a http response
    x = calculate()
    return render(request, 'hello.html', {'name' : 'Gabriele'}) # -> returns a function render with the html file as a http response

# What it's called a view in other frameworks, in django is a template (Model-View-Template)
