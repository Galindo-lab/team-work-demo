from django import forms

from core.models import BelbinProfile, EvaluationResult

# forms.py
from django import forms
from .models import Group


class JoinGroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    code = forms.CharField(widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(JoinGroupForm, self).is_valid()
        if not valid:
            return valid

        group = self.cleaned_data.get('group')
        password = self.cleaned_data.get('code')

        if group and password:
            if group.code == password:
                return True

        self.add_error('code', 'Contraseña incorrecta.')
        return False


class BelbinForm(forms.ModelForm):
    class Meta:
        model = BelbinProfile
        fields = '__all__'
