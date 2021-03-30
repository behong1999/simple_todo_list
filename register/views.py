#NOTE: https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/
from django.shortcuts import render, redirect

#NOTE: https://docs.djangoproject.com/en/3.1/topics/auth/default/
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(response,"register/register.html",{"form":form})