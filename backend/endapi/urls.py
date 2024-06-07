# urls.py

from django.urls import path
from . import views
from .views import LogListView


urlpatterns = [
    path("", views.signin_view, name="signin"),
    path("admins/", views.admins_view, name="admin"),
    path("generate_logs/", views.generate_logs_view, name="generate_logs"),
    path("log_api/", LogListView.as_view(), name="log_api"),
]
