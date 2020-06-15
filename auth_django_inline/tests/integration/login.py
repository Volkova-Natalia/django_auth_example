from rest_framework import status
from django.urls import reverse
from django.contrib.auth import authenticate

from .common import IntegrationCommonTestCase

from ...urls import namespace
from ...forms import LoginForm


# Create your tests here.
class IntegrationLoginTestCase(IntegrationCommonTestCase):
    url = reverse(namespace + ':login')

    status_code_expected = {
        'get': status.HTTP_200_OK,
        'post': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        }
    }

    template_expected = 'auth_django_inline/login.html'

    form_expected = {
        'get': LoginForm,
        'post': LoginForm,
    }

    form_valid_expected = {
        'get': None,
        'post': None,
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
        assert_message = 'integration login GET'
        super()._test_get(response, assert_message)

    def _test_post(self, response):
        assert_message = 'integration login POST'
        self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_valid_expected['post'] = self.form_expected['post'].is_valid()
        super()._test_post(response, assert_message)

        user = authenticate(username=self.user['username'], password=self.user['password'])
        self.assertNotEquals(user, None, assert_message + ' test user')
        self.assertEquals(user.is_active, True, assert_message + ' test user.is_active')

    # ======================================================================

    def execute(self):
        response = self.get()
        self._test_get(response)

        response = self.post(self.user)
        self._test_post(response)

    # ======================================================================

    def test(self):
        assert_message = 'integration login'
        pass
        # TODO

    # ======================================================================
