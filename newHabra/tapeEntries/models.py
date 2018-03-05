from django.db import models


class User(models.Model):
    login = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    lastLoginDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
        ordering = ['-login']

    def __str__(self):
        return self.login

    #def set_password(self, password):



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    createdDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'post'
        ordering = ['-createdDate']

    def __str__(self):
        return self.title + '. \tAuthor: ' + str(self.author)
