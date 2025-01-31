from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class Sign_Up_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ["password1", "password2", "username", "email"]