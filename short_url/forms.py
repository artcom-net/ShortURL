from django import forms
from django.core.validators import URLValidator


class ShortURLForm(forms.Form):
    widget = forms.TextInput(attrs={'placeholder': 'Enter a long URL'})
    url = forms.CharField(max_length=200, validators=(URLValidator(),),
                          label='', widget=widget)
