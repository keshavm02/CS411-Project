from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    last_name = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + str(self.author)


class Review(models.Model):
    overall = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)


class AuthorReview(Review):
    author = models.ForeignKey('Author', blank=False, null=False, on_delete=models.CASCADE)


class ArticleReview(Review):
    article = models.ForeignKey('Article', blank=False, null=False, on_delete=models.CASCADE)
