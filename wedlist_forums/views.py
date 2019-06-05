from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.response import Response
from .forms import NewPostForm, NewProfileForm, NewSolutionsForm
from .models import Posts, Profile, Status, Solutions


# Create your views here.
def home(request):
    current_user = request.user
    posts = Posts.get_posts()
    title = "Wedlist Forums"

    return render(request,'all/home.html', {"title":title, "posts":posts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.poster_id = current_user.id
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})


def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def profile(request):
    current_user = request.user
    posts = Posts.objects.filter(profile = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'posts':posts,'current_user':current_user})

def search_results(request):
    if 'post' in request.GET and request.GET ["post"]:
        search_term = request.GET.get("post")
        searched_posts = Posts.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'all/search.html', {"message":message, "posts":searched_posts})
    else:
        message = "You haven't searched for any posts yet!"
        return render (request, 'all/search.html', {"message": message})

def solution(request,id):
    post = Posts.objects.filter(id=id)
    current_user = request.user

    if request.method=='POST':
        form = NewSolutionsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post_id = id
            form.save()
            return redirect('solution',id)
    else:
        form=NewSolutionsForm()

    try:
        user_solution=Solutions.objects.filter(post_id=id)
    except Exception as e:
        raise Http404()
   
    return render(request, 'all/solution.html',{'post':post, 'current_user': current_user,  'form':form, 'solutions':user_solution})
