from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "nickname", "phone_number", "birth_day"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {"password": forms.PasswordInput}