from django import forms
from .models import Signin

class SigninForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = ['email', 'password', 'role']
