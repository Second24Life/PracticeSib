from django.contrib import admin
from .models import Post  # User


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'last_login')
#     list_filter = ['last_login']
#     search_fields = ['username']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'createdDate')
    list_filter = ['createdDate']
    search_fields = ['title', 'body', 'author']


# admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
