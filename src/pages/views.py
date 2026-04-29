from django.http import HttpResponse
from django.shortcuts import render
from django import VERSION # < NEU

def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request): # < NEU
    major, minor, micro, *_ = VERSION
    context = {
        "name": "Django", 
        "profession": "Python-Webframework", 
        "age": 20, 
        "current_version": f"{major}.{minor}.{micro}"
    }
    return render(request, "pages/about.html", context)
