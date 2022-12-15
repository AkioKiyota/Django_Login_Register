from django.forms import *


class LoginForm(Form):
    your_name = CharField(label='Name', max_length=100)
    your_pass = CharField(label='Password', max_length=100, widget=PasswordInput())


class RegisterForm(Form):
    your_name = CharField(label='Name', max_length=100)
    your_pass = CharField(label='Password', max_length=100, widget=PasswordInput())
