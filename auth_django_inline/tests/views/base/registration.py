from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse

from ..common import CommonTestCase

from ....urls import namespace
from ....forms import RegistrationForm
from django.contrib.auth.models import User


# Create your tests here.
class BaseRegistrationTestCase(CommonTestCase):
    url = reverse(namespace + ':registration')

    status_code_expected = {
        'get': status.HTTP_200_OK,
        'post': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        }
    }

    template_expected = 'auth_django_inline/registration.html'

    form_expected = {
        'get': RegistrationForm,
        'post': RegistrationForm,
    }

    form_valid_expected = {
        'get': None,
        'post': None,
    }

    action_expected = 'registration'

    message_expected = {
        'get': None,
        'post': {
            'success': 'You successfully registered.',
            'fail': None,
        }
    }

    # ======================================================================

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user=user, *args, **kwargs)
        # self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_expected['post'] = RegistrationForm(self.user)
        self.form_valid_expected['post'] = self.form_expected['post'].is_valid()

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def get(self):
        response = super().get(self.url)
        return response

    # def post(self, user=None):
    def post(self):
        # response = super().post(self.url, user)
        response = super().post(self.url, self.user)
        return response

    # ======================================================================

    def _test_get(self, response, assert_message=''):
        assert_message = assert_message + ' registration GET'
        super()._test_get(response, assert_message)

    def _test_post(self, response, assert_message=''):
        assert_message = assert_message + ' registration POST'
        super()._test_post(response, assert_message)

    # ======================================================================
