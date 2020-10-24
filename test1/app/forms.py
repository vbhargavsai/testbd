from django import forms
from .models import tester

# Create your tests here.


class testing(forms.ModelForm):
    class Meta:
        model=tester
        fields="__all__"
