from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from profiles.forms import Register_User_Form
from profiles.models import User_Profile


def register_user(request):
    if request.method == 'POST':
        form = Register_User_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]

            about = form.cleaned_data["about"]
            phone_num = form.cleaned_data["phone_num"]
            picture_url = form.cleaned_data["picture_url"]

            print('user created')
            user = User.objects.get(username)
            print('user authenticated')
            # user.user_profile.phone_num
            User_Profile.objects.create(user=user, about=about, phone_num=phone_num, picture_url=picture_url)
            print('user profile created')
            login(request, user)
            print('login successfull')
            messages.success(request, "Registration Successfull")
            return redirect('/')
    else:
        form = Register_User_Form()

    return render(request, 'registration/register.html', {"form": form})
