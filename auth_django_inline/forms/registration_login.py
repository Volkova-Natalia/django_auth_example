from django import forms
from django.contrib.auth.models import User


class RegistrationLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def get_user(self, username):
        print('RegistrationLoginForm.get_user(', username, ')', sep='')
        try:
            user = User.objects.get(username=username)
            return user
        except:
            return None

    def is_user_exists(self, username):
        print('RegistrationLoginForm.is_user_exists(', username, ')', sep='')
        if self.get_user(username):
            return True
        else:
            return False
