from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# EXCEPTION
from django.db.utils import IntegrityError


def Register_User(user_name, user_pass):
    try:
        created_user = User.objects.create_user(user_name, None, user_pass)
        created_user.save()
    except IntegrityError:
        return None

    return user_name


def Login_User(request, user_name, user_pass):
    user = authenticate(username=user_name, password=user_pass)
    if user is not None:
        # GIVE ACCESS
        login(request, user)
        return True
    else:
        # DON'T GIVE ACCESS
        return False


def Logout_User():
    pass
