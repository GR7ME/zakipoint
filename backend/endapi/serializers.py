from rest_framework import serializers
from .models import Admins, Signin


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = ["id", "email", "password", "role"]


class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ["id", "email", "password"]
