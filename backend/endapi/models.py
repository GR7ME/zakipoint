from django.db import models

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