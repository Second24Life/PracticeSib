from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Post
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login


def index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {'posts': posts})


def profile(request, id):
    return HttpResponse("<h2>Profile {}</h2>".format(id))


def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(login=cd['login'])

            if user.check_password(cd['password']):
                login(request, user)
                return render(request, "post/index.html")
    else:
        form = LoginForm()

    return render(request, "user/auth.html", {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'user/auth.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, "user/register.html", {'user_form': user_form})


def add_post(request):
    return HttpResponse("<h2>Add_post</h2>")


def edit_post(request, id):
    return HttpResponse("<h2>Edit_post {}</h2>".format(id))
