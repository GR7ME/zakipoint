# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('signin/', views.signin_view, name='signin'),
    path('admins/',views.admins_view,name='admin'),
]
