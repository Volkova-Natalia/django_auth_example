from rest_framework import status
from django.urls import reverse

from .common import IntegrationCommonTestCase

from ...urls import namespace
from ...forms import RegistrationForm


# Create your tests here.
class IntegrationRegistrationTestCase(IntegrationCommonTestCase):
    url = reverse(namespace + ':registration')

    template_expected = 'auth_django_inline/registration.html'

    form_expected = {
        'get': RegistrationForm,
        'post': None,   # TODO
    }

    action_expected = 'registration'

    message_expected = {
        'get': None,
        'post': {
            'success': 'You successfully registered.',
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
        assert_message = 'integration registration get'
        self.assertEquals(response.status_code, status.HTTP_200_OK, assert_message)
        self._test_template(response, self.template_expected, assert_message)
        self._test_form(response, self.form_expected['get'], assert_message)
        self._test_action(response, self.action_expected, assert_message)
        self._test_message(response, self.message_expected['get'], assert_message)

    def _test_post(self, response):
        assert_message = 'integration registration post'
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
        assert_message = 'integration registration'
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! integration registration\n')
        pass
        # TODO

    # ======================================================================
