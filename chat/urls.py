from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.HomeView, name="home"),
    path("<uuid:uuid>", views.GroupChatView, name="group")
]