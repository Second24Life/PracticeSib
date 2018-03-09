from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import UserRegistrationForm  # , LoginForm
# from django.contrib.auth import logout, authenticate, login,
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    user = get_object_or_404(User, pk=id)
    queryset = user.posts.order_by('-createdDate')
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'user/profile.html', {'user': user, 'posts': posts})


# def auth(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 username=cd['username'], password=cd['password'])

#             if user is not None:
#                 login(request, user)
#                 return HttpResponsePermanentRedirect('/')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()

#     return render(request, "user/auth.html", {'form': form})


# def logout(request):
#     logout(request)
#     return HttpResponsePermanentRedirect('auth/')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return HttpResponsePermanentRedirect('/auth/')
    else:
        user_form = UserRegistrationForm()

    return render(request, "user/register.html", {'user_form': user_form})


def add_post(request):
    return HttpResponse("<h2>Add_post</h2>")


def edit_post(request, id):
    return HttpResponse("<h2>Edit_post {}</h2>".format(id))
