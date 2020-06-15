from rest_framework import status
from django.urls import reverse

from .common import IntegrationCommonTestCase

from ...urls import namespace
from ...forms import LoginForm


# Create your tests here.
class IntegrationLoginTestCase(IntegrationCommonTestCase):
    url = reverse(namespace + ':login')

    template_expected = 'auth_django_inline/login.html'

    form_expected = {
        'get': None,   # TODO
        'post': None,   # TODO
    }

    action_expected = 'login'

    message_expected = {
        'get': None,
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

    def _test_get(self, response):
        assert_message = 'integration login get'
        pass
        # TODO

    def _test_post(self, response):
        assert_message = 'integration login post'
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
        assert_message = 'integration login'
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! integration login\n')
        pass
        # TODO

    # ======================================================================
