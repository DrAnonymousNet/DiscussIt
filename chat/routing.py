from django.urls import re_path,path

from . import consumers

websocket_urlpatterns = [
    path('', consumers.JoinAndLeave.as_asgi()),
    path('groups/<uuid:uuid>/',consumers.GroupConsumer.as_asgi())
]