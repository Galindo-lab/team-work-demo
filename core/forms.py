from django import forms

from core.models import BelbinProfile, GroupForm

# forms.py
from django import forms
from .models import Group


class JoinGroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label="Seleccione un grupo")


class BelbinForm(forms.ModelForm):
    class Meta:
        model = BelbinProfile
        fields = '__all__'
