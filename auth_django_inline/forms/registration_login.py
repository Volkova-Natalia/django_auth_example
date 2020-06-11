from django import forms
from django.contrib.auth.models import User


class RegistrationLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
