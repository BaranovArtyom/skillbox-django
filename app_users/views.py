from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_users.forms import *
from app_users.models import Profile
import datetime
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if not (datetime.datetime.now().hour in range(22, 25) or
                        datetime.datetime.now().hour in range(0, 9)):
                    if not user.is_superuser:
                        if user.is_active:
                            login(request, user)
                            return HttpResponse('SUCCESS')
                        else:
                            auth_form.add_error('__all__', 'User is inactive!')
                    else:
                        auth_form.add_error('__all__', 'User is admin!!')
                else:
                    auth_form.add_error('__all__', 'Go sleep man!')
            else:
                auth_form.add_error('__all__', 'Incorrect data!')

    else:
        auth_form = AuthForm()
    context = {'form': auth_form}
    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('You logged out!')


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def another_register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'users/register.html', {'form': form})
