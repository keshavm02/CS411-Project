from sys import stderr

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import JsonResponse
from django import forms

from .models import *


def index(request):
    context = {

    }
    return render(request, 'main/index.html', context)


def author(request):
    data = {

    }
    return JsonResponse(data)


def article(request):
    data = {

    }
    return JsonResponse(data)


def search(request):
    data = {

    }
    return JsonResponse(data)


def user_auth(request):
    class UserForm(forms.Form):
        validated = forms.BooleanField()
        username = forms.CharField()
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.CharField()

    if request.user.is_authenticated:
        data = {
            'validated': True,
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
    else:
        data = {
            'validated': False
        }
    form = UserForm(data)
    context = {
        'form': form
    }
    return render(request, 'main/authentication.html', context)


def deauth(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
            else:
                try:
                    user = User.objects.create_user(request.POST['username'], request.POST['email'],
                                                    request.POST['password'])
                    login(request, user)
                except Exception as e:
                    pass
        except Exception as e:
            pass
    context = {
    }
    return render(request, 'main/register.html', context)
