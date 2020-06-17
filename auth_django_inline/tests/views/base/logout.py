from rest_framework import status
from django.urls import reverse

from ..common import CommonTestCase

from ....settings import namespace


# Create your tests here.
class BaseLogoutTestCase(CommonTestCase):
    url = reverse(namespace + ':logout')

    """
    Only for logout - redirect.
    """
    _response_url_expected = reverse(namespace + ':login') + '?next=' + url
    response_url_expected = {
        'get': {
            'success': None,
            'fail': _response_url_expected,
        },
        'post': {
            'success': None,
            'fail': _response_url_expected,
        }
    }

    status_code_expected = {
        'get': {
            'success': status.HTTP_200_OK,
            'fail': status.HTTP_302_FOUND,
        },
        'post': {
            'success': status.HTTP_200_OK,
            'fail': status.HTTP_302_FOUND,
        }
    }

    _template_expected = 'auth_django_inline/logout.html'
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
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
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
            'success': None,
            'fail': None,
        }
    }

    _action_expected = 'logout'
    action_expected = {
        'get': {
            'success': _action_expected,
            'fail': None,
        },
        'post': {
            'success': _action_expected,
            'fail': None,
        }
    }

    message_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': 'You successfully logged out.',
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

    def get(self, client=None):
        client, response = super().get(client=client, url=self.url)
        return client, response

    def post(self, client=None):
        client, response = super().post(client=client, url=self.url, data=self.user)
        return client, response

    # ======================================================================

    def _test_get(self, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + success_fail + ' logout GET'
        super()._test_get(response, success_fail, assert_message)

        if success_fail == 'fail':
            self.assertEquals(response.url,
                              self.response_url_expected['get'][success_fail],
                              assert_message + ' response.url')

    def _test_post(self, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + success_fail + ' logout POST'
        super()._test_post(response, success_fail, assert_message)

    # ======================================================================
