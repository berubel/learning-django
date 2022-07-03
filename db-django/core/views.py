from django.shortcuts import render, HttpResponse

# Create your views here.

def hello (request, name, years) :
    return HttpResponse('<h1> Hello World!!</h1> <br> '
                        '<h2> Student: {}, {} years old.</h2>'.format(name, years))


def sum(request, num1, num2):
    result = num1 + num2
    return HttpResponse('<h1>Sum</h1> <br>'
                            '{} + {} = {}'.format(num1, num2, result))

def sub(request, num1, num2):
    result = num1 - num2
    return HttpResponse('<h1>Subtraction</h1> <br>'
                        '{} - {} = {}'.format(num1, num2, result))

def div(request, num1, num2):
    result = num1 / num2
    return HttpResponse('<h1>Division</h1> <br>'
                        '{} / {} = {}'.format(num1, num2, result))

def mult(request, num1, num2):
    result = num1 * num2
    return HttpResponse('<h1>Multiplication</h1> <br>'
                            '{} * {} = {}'.format(num1, num2, result))