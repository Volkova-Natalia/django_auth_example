from django import forms
from .registration_login import RegistrationLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginForm(RegistrationLoginForm):
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError(
                'The username or password is not correct.'
            )
        else:
            if not user.is_active:
                raise forms.ValidationError(
                    'The user is disabled.'
                )
            else:
                return self.cleaned_data

    def login(self, request):
        user = authenticate(username=self.cleaned_data['username'],
                            password=self.cleaned_data['password'])
        login(request, user)
