from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SigninForm
from .models import Admins
from django.contrib.auth.models import User
# Create your views here.
# views.py

def hello_world(request):
    return HttpResponse("Testing Phase")

def signin_view(request):
    return HttpResponse('Data save Successfully')

def admins_view(request):
    return HttpResponse('Admins') 

