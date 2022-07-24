from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import (login, logout)
#from channels.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def LoginView(request:HttpRequest):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse("chat:home"))
    context = {
        "form":form
    }
    return render(request, template_name="account/login.html", context=context)


def LogoutView(request:HttpRequest):
    '''
    The view logout the user and redirect them to the login page
    '''
    logout(request)
    return redirect(reverse("chat:login"))

def SignUpView(request:HttpRequest):
    '''
    A view for users to sign up
    '''
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse("account:login"))
    context = {
        "form":form
    }
    return render(request, template_name="account/signup.html", context=context)

