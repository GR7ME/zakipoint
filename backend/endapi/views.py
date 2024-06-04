from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SigninForm
from .models import Admins
# Create your views here.
# views.py

def hello_world(request):
    return HttpResponse("Testing Phase")

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

def admins_view(request):
    predefined_email = "admin@gmail.com"
    predefined_password = "password123"
    admin_exists = Admins.objects.filter(email=predefined_email).exists()
    if not admin_exists:
        # Create a new instance of the Admin model with predefined values
        admin = Admins(email=predefined_email, password=predefined_password)
        admin.save()
    return redirect('Admin') 


