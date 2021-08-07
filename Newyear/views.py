import datetime
from django.shortcuts import render

# Create your views here.
def index(request): 
   now = datetime.datetime.now()
   
   return render(request, "Newyear/index.html", {
      "Newyear": now.month == 1 & now.day == 1
   })