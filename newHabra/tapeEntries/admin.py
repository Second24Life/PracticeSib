from django.contrib import admin
from .models import User, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'lastLoginDate')
    list_filter = ['lastLoginDate']
    search_fields = ['login']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'createdDate')
    list_filter = ['createdDate']
    search_fields = ['title', 'body', 'author']


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
