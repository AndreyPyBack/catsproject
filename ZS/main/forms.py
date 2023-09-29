from django import forms
from .models import Cats


class CatsModelForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name']