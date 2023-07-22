
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Profile, Group, ProfileForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': ''
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': '',
            'placeholder': ''
        })
    )


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


class BelbinForm(forms.ModelForm):

    class Meta:
        model = ProfileForm
        fields = [
            'resource_investigator',
            'team_worker',
            'coordinator',
            'plant',
            'monitor_evaluator',
            'specialist',
            'shaper',
            'implementer',
            'completer_finisher',
        ]
