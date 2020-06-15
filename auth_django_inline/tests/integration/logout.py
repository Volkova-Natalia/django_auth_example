from rest_framework import status
from django.urls import reverse

from .common import IntegrationCommonTestCase

from ...urls import namespace
# from ...forms import LogutForm


# Create your tests here.
class IntegrationLogoutTestCase(IntegrationCommonTestCase):
    url = reverse(namespace + ':logout')

    template_expected = 'auth_django_inline/logout.html'

    form_expected = {
        'get': None,   # TODO
        'post': None,   # TODO
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
        assert_message = 'integration logout get'
        pass
        # TODO

    def _test_post(self, response):
        assert_message = 'integration logout post'
        pass
        # TODO

    # ======================================================================

    def execute(self, user=None):
        response = self.get()
        self._test_get(response)

        response = self.post(user)
        self._test_post(response)

    # ======================================================================

    def test(self, user=None):
        assert_message = 'integration logout'
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! integration logout\n')
        pass
        # TODO

    # ======================================================================
