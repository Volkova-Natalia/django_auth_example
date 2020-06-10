from django import forms
from django.contrib.auth.models import User


class RegistrationLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
            return user
        except:
            return None

    def is_user_exists(self, username):
        if self.get_user(username):
            return True
        else:
            return False
