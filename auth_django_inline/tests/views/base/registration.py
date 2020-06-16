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
        'get': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        },
        'post': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        }
    }

    _template_expected = 'auth_django_inline/registration.html'
    template_expected = {
        'get': {
            'success': _template_expected,
            'fail': None,   # TODO
        },
        'post': {
            'success': _template_expected,
            'fail': _template_expected,
        }
    }

    form_expected = {
        'get': {
            'success': RegistrationForm,
            'fail': None,   # TODO
        },
        'post': {
            'success': RegistrationForm,
            'fail': RegistrationForm,
        }
    }

    form_expected_valid = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    form_expected_valid_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': True,
            'fail': None,
        }
    }

    _action_expected = 'registration'
    action_expected = {
        'get': {
            'success': _action_expected,
            'fail': _action_expected,
        },
        'post': {
            'success': _action_expected,
            'fail': _action_expected,
        }
    }

    message_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': 'You successfully registered.',
            'fail': None,
        }
    }

    # ======================================================================

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user=user, *args, **kwargs)
        # self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_expected['post']['success'] = RegistrationForm(self.user)
        # self.form_valid_expected['post'] = self.form_expected['post'].is_valid()
        self.form_expected_valid['post']['success'] = self.form_expected['post']['success'].is_valid()

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
