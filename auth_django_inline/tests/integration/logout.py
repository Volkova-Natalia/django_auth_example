from rest_framework import status
from django.urls import reverse

from .common import IntegrationCommonTestCase

from ...urls import namespace
# from ...forms import LogutForm


# Create your tests here.
class IntegrationLogoutTestCase(IntegrationCommonTestCase):
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

    def _test_get(self, response):
        assert_message = 'integration logout GET'
        # super()._test_get(response, assert_message)

    def _test_post(self, response):
        assert_message = 'integration logout POST'
        # super()._test_post(response, assert_message)
        # TODO

    # ======================================================================

    def execute(self):
        response = self.get()
        self._test_get(response)

        response = self.post(self.user)
        self._test_post(response)

    # ======================================================================

    def test(self):
        assert_message = 'integration logout'
        pass
        # TODO

    # ======================================================================
