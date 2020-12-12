from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author', views.author, name='author'),
    path('article', views.article, name='article'),
    path('search', views.search, name='search'),
    path('login', views.auth, name='login'),
    path('logout', views.deauth, name='logout'),
    path('register', views.register, name='register'),
]