from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def profile(request, id):
    return HttpResponse("<h2>Profile {}</h2>".format(id))

def auth(request):
    return render(request, "auth.html")

def register(request):
    return render(request, "register.html")

def add_post(request):
    return HttpResponse("<h2>Add_post</h2>")

def edit_post(request, id):
    return HttpResponse("<h2>Edit_post {}</h2>".format(id))