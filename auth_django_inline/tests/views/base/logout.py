from rest_framework import status
from django.urls import reverse

from ..common import CommonTestCase

from ....urls import namespace
# from ....forms import LogutForm


# Create your tests here.
class BaseLogoutTestCase(CommonTestCase):
    url = reverse(namespace + ':logout')

    status_code_expected = {
        'get': status.HTTP_200_OK,
        'post': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        }
    }

    template_expected = 'auth_django_inline/logout.html'

    form_expected = {
        'get': None,   # TODO
        'post': None,   # TODO
    }

    form_valid_expected = {
        'get': None,
        'post': None,
    }

    action_expected = 'logout'

    message_expected = {
        'get': None,    # TODO
        'post': {
            'success': None,    # TODO,
            'fail': None,   # TODO
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
        assert_message = assert_message + ' ' + success_fail + ' logout GET'
        # super()._test_get(response, success_fail, assert_message)

    def _test_post(self, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + success_fail + ' logout POST'
        # super()._test_post(response, success_fail, assert_message)
        # TODO

    # ======================================================================
