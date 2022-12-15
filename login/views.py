from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from .users import Login_User, Register_User, Logout_User


def index(request):
    if request.method == 'POST' and 'Login' in request.POST:
        return HttpResponseRedirect("login")

    if request.method == 'POST' and 'Register' in request.POST:
        return HttpResponseRedirect("register")

    return render(request, "main/main.html", {})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['your_name']
            user_pass = form.cleaned_data['your_pass']

            user = Login_User(request, user_name, user_pass)
            if user:
                return render(request, "main/home.html", {'name': user_name})
            else:
                return render(request, "main/login.html", {'form': form, 'warning': True})

    else:
        form = LoginForm()

    return render(request, "main/login.html", {'form': form, 'warning': False})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['your_name']
            user_pass = form.cleaned_data['your_pass']

            created_user = Register_User(user_name, user_pass)
            if created_user is not None:
                return render(request, "main/home.html", {'name': form.cleaned_data['your_name']})
            else:
                return render(request, "main/register.html", {'form': form, 'warning': True})

    else:
        form = RegisterForm()

    return render(request, "main/register.html", {'form': form, 'warning': False})


def home(request):
    if request.method == 'POST' and 'Logout' in request.POST:
        print('logout')
        Logout_User()

        return render(request, "main/base.html", {})
    return render(request, "main/home.html", {})
