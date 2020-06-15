from rest_framework import status
from django.urls import reverse
from django.contrib.auth import authenticate

from .common import IntegrationCommonTestCase

from ...urls import namespace
from ...forms import LoginForm


# Create your tests here.
class IntegrationLoginTestCase(IntegrationCommonTestCase):
    url = reverse(namespace + ':login')

    template_expected = 'auth_django_inline/login.html'

    form_expected = {
        'get': LoginForm,
        'post': LoginForm,
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

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

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
        self.assertEquals(response.status_code, status.HTTP_200_OK, assert_message + ' test status_code')

        self._test_template(response, self.template_expected, assert_message + ' test template')
        self._test_form(response, self.form_expected['get'], assert_message + ' test form')
        self._test_action(response, self.action_expected, assert_message + ' test action')
        self._test_message(response, self.message_expected['get'], assert_message + ' test message')

    def _test_post(self, response):
        assert_message = 'integration login POST'
        self.assertEquals(response.status_code, status.HTTP_200_OK, assert_message + ' test status_code')

        self._test_template(response, self.template_expected, assert_message + ' test template')
        self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_valid_expected = self.form_expected['post'].is_valid()
        self.assertEquals(self.form_valid_expected, True, assert_message + ' test form_valid')
        self._test_form(response, self.form_expected['post'], assert_message + ' test form')
        self._test_action(response, self.action_expected, assert_message + ' test action')
        self._test_message(response, self.message_expected['post']['success'], assert_message + ' test message')

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
