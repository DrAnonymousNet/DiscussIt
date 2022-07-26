from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db.models import QuerySet
from .models import Group

def get_online_user(group:Group) -> QuerySet:
    '''An Helper function to get a list of logged in users from non expired session'''
    sessions = Session.objects.filter(expire_date__gte = timezone.now())
    uid_list = []

    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get("_auth_user_id", None))

    return group.members.filter(id__in = uid_list)