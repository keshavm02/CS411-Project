from sys import stderr

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login


def index(request):
    context = {
    }
    return render(request, 'main/index.html', context)


def author(request):
    context = {
    }
    return render(request, 'main/author.html', context)


def article(request):
    context = {
    }
    return render(request, 'main/article.html', context)


def search(request):
    context = {
    }
    return render(request, 'main/search.html', context)


def auth(request):
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
        except Exception as e:
            pass

    context = {
    }
    return render(request, 'main/login.html', context)


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
