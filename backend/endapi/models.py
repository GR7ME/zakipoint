from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Signin(models.Model):
    ADMIN = 'admin'
    USER = 'user'
    
    role_choice = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)
    role = models.CharField(max_length=250,choices=role_choice)

class Admins(models.Model):
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)



# class Admins(models.Model):
#     DEFAULT_EMAIL = "admin@gmail.com"
#     DEFAULT_PASSWORD = "password123"
#     email = models.EmailField(max_length=250, default=DEFAULT_EMAIL)
#     password = models.CharField(max_length=250, default=make_password(DEFAULT_PASSWORD))