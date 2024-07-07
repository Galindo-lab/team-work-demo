from django import forms

from core.models import BelbinProfile


class BelbinForm(forms.ModelForm):
    class Meta:
        model = BelbinProfile
        fields = '__all__'
