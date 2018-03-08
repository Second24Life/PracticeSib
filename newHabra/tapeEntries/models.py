from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password, make_password


# class User(models.Model):
#    login = models.CharField(max_length=40, unique=True)
#    password = models.CharField(max_length=100)
#    last_login = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'user'
#         ordering = ['-login']

#     def is_authenticated(self):
#         return True

#     def set_password(self, raw_password):
#         try:
#             self.password = make_password(raw_password)
#         except Exception as e:
#             raise e

#     def check_password(self, raw_password):
#         if check_password(raw_password, self.password):
#             return True
#         else:
#             return False

#     def __str__(self):
#         return self.login


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=10000)
    author = models.ForeignKey(
        User, related_name='posts', null=True, on_delete=models.SET_NULL)
    createdDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'post'
        ordering = ['-createdDate']

    def __str__(self):
        return self.title + '. \tAuthor: ' + str(self.author.username)
