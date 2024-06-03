from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SigninForm
# Create your views here.
# views.py

def hello_world(request):
    return HttpResponse("Hello, World!")

def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
             
             email = form.cleaned_data['email']
             password = form.cleaned_data['password']
             role = form.cleaned_data['role']
             user = authenticate(request, email=email, password=password)
             form.save()
            # Redirect to a success page or do something else
             return redirect('success')
    else:
        form = SigninForm()
    return HttpResponse('Data save Successfully')


