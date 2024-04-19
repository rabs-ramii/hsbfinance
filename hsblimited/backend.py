from hsblimited.models import User
from django.shortcuts import redirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.hashers import check_password


def authenticate(request, username=None, password=None):
    user = User.objects.filter(email=username).values()
    try:
        dbPass = user[0]["password"]
        password_match = check_password(password, dbPass)
        if password_match:
            return user
        else:
            return None
    except:
        return None


def login(request, user):
    session = SessionStore()
    session['username'] = user[0]["email"]
    session["name"] = user[0]["fullname"]
    session.save()
    request.session = session


def logout(request):
    request.session.flush()


