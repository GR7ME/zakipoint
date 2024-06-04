from django.contrib import admin

# Register your models here.
from .models import(
    Signin,
    Admins
)
admin.site.register(Signin)
admin.site.register(Admins)