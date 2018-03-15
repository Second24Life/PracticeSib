import json
import urllib.request
from django.http import HttpResponsePermanentRedirect  # , HttpResponse
from django.shortcuts import get_object_or_404, render  # , redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import UserRegistrationForm, AddPostForm, EditPostForm, LoginForm


def index(request):
    queryset = Post.objects.order_by('-createdDate')
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "post/index.html", {'posts': posts})


@login_required
def profile(request, id):
    author = get_object_or_404(User, pk=id)
    queryset = author.posts.order_by('-createdDate')
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'user/profile.html', {'user': request.user,
                                                 'author': author,
                                                 'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()

                return HttpResponsePermanentRedirect('/auth/')
            else:
                return render(request, "user/register.html", {'form': form})

    else:
        form = UserRegistrationForm()

    return render(request, "user/register.html", {'form': form})


def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    recaptcha_response = request.POST.get(
                        'g-recaptcha-response')
                    url = 'https://www.google.com/recaptcha/api/siteverify'
                    values = {
                        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': recaptcha_response
                    }
                    data = urllib.parse.urlencode(values).encode()
                    req = urllib.request.Request(url, data=data)
                    response = urllib.request.urlopen(req)
                    result = json.loads(response.read().decode())

                    if result['success']:
                        login(request, user)
                        return HttpResponsePermanentRedirect('/')
                    else:
                        return render(request, "user/auth.html",
                                      {'form': form})
    else:
        form = LoginForm()
    return render(request, 'user/auth.html', {'form': form})


@login_required
def get_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post/post.html', {'post': post})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'post/post.html', {'post': post})
    else:
        form = AddPostForm()
    return render(request, 'post/add_post.html', {'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'post/post.html', {'post': post})
    else:
        form = EditPostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    author_id = post.author.id
    post.delete()

    return HttpResponsePermanentRedirect('/profile/{}/'.format(author_id))
