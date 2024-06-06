from django.db import models
# from django.contrib.auth.hashers import make_password

# Create your models here.


class Signin(models.Model):
    ADMIN = "admin"
    USER = "user"

    role_choice = [
        (ADMIN, "Admin"),
        (USER, "User"),
    ]
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)
    role = models.CharField(max_length=250, choices=role_choice)


class Admins(models.Model):
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)


class LogEntry(models.Model):
    timestamp = models.DateTimeField()
    message_status = models.CharField(max_length=10)
    message = models.TextField()
    log_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.message_status} - {self.message}"


# class Admins(models.Model):
#     DEFAULT_EMAIL = "admin@gmail.com"
#     DEFAULT_PASSWORD = "password123"
#     email = models.EmailField(max_length=250, default=DEFAULT_EMAIL)
#     password = models.CharField(max_length=250, default=make_password(DEFAULT_PASSWORD))
