from os import name
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
from .forms import CreateNewList
# Create your views here.

def index(response,id):
    ls = ToDoList.objects.get(id=id)
    # item = ls.item_set.get(id = id)
    # NOTE: return HttpResponse(f'<h1>{id}</h1>')
    # or
    # return HttpResponse("<h1>%s</h1><br><p>%s</p>"%(ls.name,str(item.txt)))
    
    # REVIEW whether the accessed to-do list truly belongs to the current user or not.
    if ls in response.user.todolist_set.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("check_"+str(item.id))=="clicked":
                        item.complete = True
                    else: 
                        item.complete = False
                    item.save()
                    
            elif response.POST.get("newItem"):
                text = response.POST.get("new")
                #NOTE: The text at least has 3 characters
                if len(text) > 2:
                    ls.item_set.create(txt=text,complete=False)
                else:
                    print("Invalid")
        return render(response,"main/list.html",{"list":ls})
    return render(response,"main/home.html",{"list":ls})


def home(response):
    return render(response,"main/home.html",{})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            #NOTE: form.cleaned_data returns a dict of validated form input files and their values
            # Hence form.is_valid needs to be called before it.
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist_set.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response,"main/create.html",{"form":form})

def view(response):
    return render(response,"main/view.html",{})