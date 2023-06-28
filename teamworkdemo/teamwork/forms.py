from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Profile, Group, BelbinUserProfile

import json


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
        model = BelbinUserProfile
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

# class BelbinForm(forms.ModelForm):
#     """
#     Formulario de belbin
#     """

#     def __init__(self, *args, **kwargs):
#         super(BelbinForm, self).__init__(*args, **kwargs)

    # Utilizar meta programacion para no tener que harcodear cada
    # campo del formulario
