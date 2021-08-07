from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return HttpResponse("Hello World")
    

def login(request): 
   return render(request, "pages/login.html",{
      "title": "Welcome"
   })