from django.db import models

class User(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    lastLoginDate = models.DateTimeField(auto_now_add=False, auto_now=True)

class Post(models.Model):
    name = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    createDate = models.DateField(auto_now_add=True, auto_now=False)
