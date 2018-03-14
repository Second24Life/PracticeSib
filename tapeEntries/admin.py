from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'createdDate')
    list_filter = ['createdDate']
    search_fields = ['title', 'body', 'author']


admin.site.register(Post, PostAdmin)
