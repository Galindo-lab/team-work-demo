from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member, Group


class UserRegisterForm(UserCreationForm):
    # la plantilla es "register.html"
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]



class CreateGroupForm(forms.ModelForm):

    class Meta: 
        model = Group
        fields = [
            'name'
        ]
