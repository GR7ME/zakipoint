from rest_framework import serializers
from .models import Admins

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['id', 'email','password']
