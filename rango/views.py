from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> Link to about page: <a href='/rango/about/'>About</a> ")

def about(request):
    return HttpResponse("Rango says here is the about page. <br/> Link back to home page: <a href='/rango/'>Index</a> ")


