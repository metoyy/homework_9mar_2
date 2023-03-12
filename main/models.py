import io

from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(max_length=3)
    registered_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.last_name} AKA {self.username}, {self.registered_at}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1024)
    author = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='post_author', null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField(max_length=255)
    author = models.ForeignKey('Person', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
