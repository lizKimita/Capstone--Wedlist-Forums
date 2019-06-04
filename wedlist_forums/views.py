from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.
def home(request):
    current_user = request.user
    # projects = Projects.get_projects()
    title = "Wedlist Forums"

    return render(request,'all/home.html', {"title":title,})

