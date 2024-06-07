from rest_framework import serializers
from .models import Admins, Signin, LogEntry


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = ["id", "email", "password", "role"]


class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ["id", "email", "password"]



class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'