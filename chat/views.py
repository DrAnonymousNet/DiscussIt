from email import message
from tokenize import group
from django.shortcuts import render, get_object_or_404
from .models import Group, Message,Event
from django.contrib.auth.decorators import login_required

@login_required
def HomeView(request):
    '''The home page where all groups are listed'''
    groups = Group.objects.all()
    user = request.user
    context = {
        "groups":group,
        "user":user
    }
    return render(request,template_name="chat/home.html",context=context)

def GroupChatView(request, uuid):
    group = get_object_or_404(Group, uuid=uuid)
    messages = group.message_set.all()
    events = group.event_set.all()

    #Combine the events and messages in for a group
    message_and_event_list = [*messages, *events]
    # Sort the combination by the timestamp so that they are listed in order
    sorted(message_and_event_list, key=lambda x : x.timestamp)

    group_members = group.members.all()
    active_members = group.members.filter()

    

