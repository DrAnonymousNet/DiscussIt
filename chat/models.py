
from pyexpat import model
from tokenize import group
from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

from django.urls import reverse
# Create your models here.

User = get_user_model()

class Group(models.Model):
    '''
    The group model where multiple users can share and discuss ideas.
    '''
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f"Group {self.name}-{self.uuid}"

    def get_absolute_url(self):
        return reverse("group", args=[str(self.uuid)])

    def add_user_to_group(self, user:User):
        '''A helper function to add a user to a group and create and event object'''
        self.members.add(user)
        self.event_set.create(type="Join", user=user)
        self.save()

    def remove_user_from_group(self, user:User):
        '''An helper function to remove user from group members when they leave the group'''
        self.members.remove(user)
        self.event_set.create(type="Left", user=user)
        self.save()


        

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group = models.ForeignKey(Group ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Messgae {self.author}-{self.group}-{self.content}"



class Event(models.Model):
    '''
    An event model that holds all event related to a group like when a user join the group or left.
    '''
    CHOICES = [
        ("Join", "join"),
        ("Left", "left")
    ]
    type = models.CharField(choices=CHOICES, max_length=10)
    description= models.CharField(help_text="A description of the event that occured", max_length=50, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group ,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.description = f"{self.user} {self.type} the {self.group.name} group"
        super().save(*args, kwargs)

    
    def __str__(self) -> str:
        return f"Event - {self.description}"

class LoggedIn(models.Model):
    STATUS=[
        ("Online","online"),
        ("Offline","offline")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10)

