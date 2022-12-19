from django.db.models import *
from django.contrib.auth.models import User


class User_Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, default="", null=True, blank=True)

    picture_url = CharField(max_length=120, default="")
    about = CharField(max_length=250, default="")
    phone_num = CharField(max_length=15, default="")

