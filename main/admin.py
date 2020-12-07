from .models import *
from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
    search_fields = ['last_name', 'first_name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'author']


@admin.register(AuthorReview)
class AuthorReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'overall']
    search_fields = ['author', 'overall']


@admin.register(ArticleReview)
class ArticleReviewAdmin(admin.ModelAdmin):
    list_display = ['article', 'overall']
    search_fields = ['article', 'overall']
