import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
from channels.auth import get_user
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from .models import Event, Message, Group
'''
async def JoinAndLeave(scope, receive, send):
    event = await receive()
    print(name_that_thing(event["type"]))
    
    #print(scope.values())
    print(event.items())

'''
class JoinAndLeave(WebsocketConsumer):

    def connect(self):
        
        self.accept()

        pass


    def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)
        type =  text_data.get("type",None)
        if type:
            data = text_data.get("data", None)
            print(text_data)
            if type == "auth_user":
                self.user = User.objects.get(id= text_data["user"])
            
            elif type == "leave_group":
                self.leave_group(data)
                
            elif type == "join_group":
                self.join_group(data)

    def leave_group(self, group_uuid):
        group = Group.objects.get(uuid=group_uuid)
        group.remove_user_from_group(self.user)
        data = {
            "type":"leave_group",
            "data":group_uuid
        }
        self.send(json.dumps(data))

    def join_group(self, group_uuid):
        group = Group.objects.get(uuid=group_uuid)
        group.add_user_to_group(self.user)
        data = {
            "type":"join_group",
            "data":group_uuid
        }
        self.send(json.dumps(data))

        
        
        


    def disconnect(self, code):
        print("Disconexted")
        pass

    def send(self, text_data=None, bytes_data=None, close=False):
        return super().send(text_data, bytes_data, close)
