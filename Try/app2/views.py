from django.shortcuts import render
from django.http import HttpResponse

def multiply(request):
    # Example multiplication logic
    a = 5
    b = 10
    result = a * b
    return HttpResponse(f"The result of {a} multiplied by {b} is {result}.")
