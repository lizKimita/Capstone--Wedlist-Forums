from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.response import Response
from .forms import NewPostForm, NewProfileForm, NewSolutionsForm, NewTipsForm,NewvotesForm, NewdownvoteForm
from .models import Posts, Profile, Status, Solutions,Tips


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
    tips = Tips.objects.filter(user = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
        user = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'posts':posts,'tips':tips,'current_user':current_user})

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


def tips(request):
    tips = Tips.get_tips()
    current_user = request.user
    try:
        pass
    except Exception as e:
        raise  Http404()
    vote = request.POST.get("like","")
    dovote = request.POST.get("dislike","")

    if request.method=='POST':
        form=NewvotesForm(request.POST)
        vote = request.POST.get("like","")
        if vote:
            like=int(vote)
            if form.is_valid:
                upvote=form.save(commit=False)
                single = Tips.objects.filter(id = vote)
                count=0
                for i in single:
                    count+=i.upvote
                total_upvotes=count+1
                Tips.objects.filter(id=vote).update(upvote=total_upvotes)
                return redirect('tips')

    else:
        forms=NewvotesForm()

    if request.method=='POST':
        form=NewdownvoteForm(request.POST)
        dovote = request.POST.get("dislike","")

        if dovote:
            dislike = int(dovote)
            if form.is_valid:
                downvote=form.save(commit=False)
                single = Tips.objects.filter(id = dovote)
                downcount=0
                for y in single:
                    downcount+=y.downvote
                total_downvotes=downcount+1
                Tips.objects.filter(id=dovote).update(downvote=total_downvotes)
                return redirect('tips')
    else:
        forms=NewdownvoteForm()

    if request.method == 'POST':
        form = NewTipsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = current_user
            form.tipper_id = current_user.id
            form.save()
        return redirect('tips')

    else:
        form = NewTipsForm()

    return render(request, 'all/tips.html', {"form": form, "tips":tips, })

