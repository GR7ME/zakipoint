from django.contrib import admin

# Register your models here.
from .models import (
    Signin,
    Admins,
    LogEntry,
)

admin.site.register(Signin)
admin.site.register(Admins)
admin.site.register(LogEntry)
