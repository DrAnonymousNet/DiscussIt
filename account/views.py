from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import (login, logout, authenticate)
from .forms import UserLoginForm
#from channels.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def LoginView(request:HttpRequest):
    form = AuthenticationForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user= form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            print(user, password)
            login(request, user)
    
            return redirect(reverse("home"))
    context = {
        "form":form
    }
    return render(request, template_name="account/login.html", context=context)


def LogoutView(request:HttpRequest):
    '''
    The view logout the user and redirect them to the login page
    '''
    logout(request)
    return redirect(reverse("login"))

def SignUpView(request:HttpRequest):
    '''
    A view for users to sign up
    '''
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            login(request, instance)
            return redirect(reverse("login"))
    context = {
        "form":form
    }
    return render(request, template_name="account/signup.html", context=context)

