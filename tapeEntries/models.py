from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField(blank=True, default='')
    author = models.ForeignKey(
        User, related_name='posts', null=True, on_delete=models.SET_NULL)
    createdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post'
        ordering = ['-createdDate']

    def __str__(self):
        return self.title + '. \tAuthor: ' + str(self.author.username)
