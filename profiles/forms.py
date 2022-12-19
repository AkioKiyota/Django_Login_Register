from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register_User_Form(UserCreationForm):
    username = CharField(label="Username", max_length=36)
    email = CharField(label="Email", max_length=120, widget=EmailInput())
    password1 = CharField(label="Password", max_length=36, widget=PasswordInput())
    password2 = CharField(label="Confirm Password", max_length=36, widget=PasswordInput())

    phone_num = CharField(label="Phone Number (optional)", max_length=15, widget=NumberInput())
    about = CharField(label="About you! (optional)", max_length=300, required=False)
    picture_url = CharField(label="Profile Photo URL (optional)", max_length=200, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",
                  "phone_num", "about", "picture_url")

    def save(self, commit=True):
        user = super(Register_User_Form, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]
        user.phone_num = self.cleaned_data["phone_num"]
        user.about = self.cleaned_data["about"]
        user.picture_url = self.cleaned_data["picture_url"]

        if commit:
            user.save()
        return user
