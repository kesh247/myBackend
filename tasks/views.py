from django import forms
from django.shortcuts import render

# Create your views here.
app_name = "tasks"
tasks = ["foo","bar", "joe"]


def index(request): 
   return render(request, "tasks/index.html",{
      "tasks": tasks
   })
   
class NewTasksForm(forms.Form): task = forms.CharField(label="New" )
   
def add(request): 
   if request.method == "POST":
      form = NewTasksForm(request.POST);
      if form.is_valid():
         task=form.cleaned_data["task"]
         tasks.append(task)
      else: 
         return render(request, "tasks/add.html", {
            "form": form
         })
         
   return render(request, "tasks/add.html", {
      "form": NewTasksForm()
   })