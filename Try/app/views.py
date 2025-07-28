from django.shortcuts import render
from django.http import HttpResponse

def my_function_view(request):
    return HttpResponse("Hello from a function-based view!")