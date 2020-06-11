from django import forms
from .registration_login import RegistrationLoginForm
from django.contrib.auth.models import User


class RegistrationForm(RegistrationLoginForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'The user with the name exists.',
                code='user_exists'
            )
        else:
            return username

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'])
        user.save()
