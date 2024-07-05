from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("this is first app")

def home1(request):
    return HttpResponse("this is second app")

    
    