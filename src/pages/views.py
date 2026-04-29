from django.http import HttpResponse
from django.shortcuts import render # << NEU

def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request): # << NEU
    return render(request, "pages/about.html")
