from tapeEntries import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

"""newHabra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('profile/<int:id>/', views.profile, name='profile'),
    #path('auth/', views.auth, name='auth'),
    path('auth/', auth_views.LoginView.as_view(template_name='user/auth.html'), name='auth'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('post/<int:id>/', views.get_post, name='get_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post')
]
