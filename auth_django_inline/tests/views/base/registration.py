from rest_framework import status
from django.urls import reverse

from ..common import CommonTestCase

from ....settings import namespace
from ....forms import RegistrationForm


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
            'fail': status.HTTP_400_BAD_REQUEST,
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
            'fail': False,
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
        self.form_expected['post']['success'] = RegistrationForm(self.user)
        self.form_expected_valid['post']['success'] = self.form_expected['post']['success'].is_valid()
        self.form_expected['post']['fail'] = RegistrationForm(self.user)
        self.form_expected_valid['post']['fail'] = self.form_expected['post']['fail'].is_valid()

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

    def post(self):
        response = super().post(self.url, self.user)
        return response

    # ======================================================================

    def _test_get(self, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + success_fail + ' registration GET'
        super()._test_get(response, success_fail, assert_message)

    def _test_post(self, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + success_fail + ' registration POST'
        super()._test_post(response, success_fail, assert_message)

    # ======================================================================
