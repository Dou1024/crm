from django.shortcuts import render, HttpResponse


# Create your views here.

def home_web(request):

    return HttpResponse("web/home")
