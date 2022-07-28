from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout"),
    path("signup/", views.SignUpView, name="signup")
]