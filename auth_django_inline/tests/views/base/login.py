from rest_framework import status
from django.urls import reverse
from django.contrib.auth import authenticate

from ..common import CommonTestCase

from ....urls import namespace
from ....forms import LoginForm


# Create your tests here.
class BaseLoginTestCase(CommonTestCase):
    url = reverse(namespace + ':login')

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

    _template_expected = 'auth_django_inline/login.html'
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
            'success': LoginForm,
            'fail': None,   # TODO
        },
        'post': {
            'success': LoginForm,
            'fail': LoginForm,
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

    _action_expected = 'login'
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
            'success': 'You successfully logged.',
            'fail': None,
        }
    }

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
        assert_message = assert_message + ' ' + success_fail + ' login GET'
        super()._test_get(response, success_fail, assert_message)

    def _test_post(self, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + success_fail + ' login POST'
        self.form_expected['post'][success_fail] = LoginForm(self.user)
        self.form_expected_valid['post'][success_fail] = self.form_expected['post'][success_fail].is_valid()
        super()._test_post(response, success_fail, assert_message)

        if success_fail == 'success':
            user = authenticate(username=self.user['username'], password=self.user['password'])
            self.assertNotEquals(user, None, assert_message + ' test user')
            self.assertEquals(user.is_active, True, assert_message + ' test user.is_active')
        elif success_fail == 'fail':
            user = authenticate(username=self.user['username'], password=self.user['password'])
            self.assertEquals(user, None, assert_message + ' test user')

    # ======================================================================
