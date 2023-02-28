#request -> response
#request handler
from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse('Hello World')

def display_form(request):
    return render(request, "entry_form.html")
