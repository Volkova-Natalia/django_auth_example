from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse

from ...urls import namespace
from ...forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your tests here.
class IntegrationTestCase(TestCase):
    url = {
        'registration': reverse(namespace + ':registration'),
        'login': reverse(namespace + ':login'),
        'logout': reverse(namespace + ':logout'),
    }

    template_expected = {
        'registration': 'auth_django_inline/registration.html',
        'login': 'auth_django_inline/login.html',
        'logout': 'auth_django_inline/logout.html',
    }

    action_expected = {
        'registration': 'registration',
        'login': 'login',
        'logout': 'logout',
    }

    test_user = {
        'username': 'username_test',
        'password': 'password_test',
    }

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def _get(self, url=''):
        client = Client()
        response = client.get(url)
        return response

    def _post(self, url='', user=test_user.copy()):
        client = Client()
        response = client.post(
            path=url,
            data=user,
            content_type='application/json'
        )
        return response

    # ======================================================================

    # ----- registration -----

    def _get_registration(self):
        response = self._get(self.url['registration'])
        return response

    def _post_registration(self, user=test_user.copy()):
        response = self._post(self.url['registration'], user)
        return response

    def _registration(self, user=test_user.copy()):
        response = self._get_registration()
        self._test_get_registration(response)

        response = self._post_registration(user)
        self._test_post_registration(response)

    # ----- login -----

    def _get_login(self):
        response = self._get(self.url['login'])
        return response

    def _post_login(self, user=test_user.copy()):
        response = self._post(self.url['login'], user)
        return response

    def _login(self, user=test_user.copy()):
        response = self._get_login()
        self._test_get_login(response)

        response = self._post_login(user)
        self._test_post_login(response)

    # ----- logout -----

    def _get_logout(self):
        response = self._get(self.url['logout'])
        return response

    def _post_logout(self, user=test_user.copy()):
        response = self._post(self.url['logout'], user)
        return response

    def _logout(self, user=test_user.copy()):
        response = self._get_logout()
        self._test_get_logout(response)

        response = self._post_logout(user)
        self._test_post_logout(response)

    # ======================================================================

    # ----- registration -----

    def _test_get_registration(self, response):
        pass
        # TODO

    def _test_post_registration(self, response):
        pass
        # TODO

    def _test_registration(self, user=test_user.copy()):
        pass
        # TODO

    # ----- login -----

    def _test_get_login(self, response):
        pass
        # TODO

    def _test_post_login(self, response):
        pass
        # TODO

    def _test_login(self, user=test_user.copy()):
        pass
        # TODO

    # ----- logout -----

    def _test_get_logout(self, response):
        pass
        # TODO

    def _test_post_logout(self, response):
        pass
        # TODO

    def _test_logout(self, user=test_user.copy()):
        pass
        # TODO

    # ======================================================================
    # clean
    # ======================================================================

    def test_registration_login_logout_clean(self):
        self._registration(self.test_user)
        self._test_registration(self.test_user)

        self._login(self.test_user)
        self._test_login(self.test_user)

        self._logout(self.test_user)
        self._test_logout(self.test_user)
        # TODO

    # ======================================================================
    # dirty
    # ======================================================================

    # ======================================================================
