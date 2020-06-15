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
        'post': RegistrationForm,
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

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_valid_expected = self.form_expected['post'].is_valid()

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
        self.assertEquals(response.status_code, status.HTTP_200_OK, assert_message)
        self._test_template(response, self.template_expected, assert_message)
        self._test_form(response, self.form_expected['post'], assert_message)
        self.assertEquals(self.form_valid_expected, True, assert_message)
        self._test_action(response, self.action_expected, assert_message)
        self._test_message(response, self.message_expected['post']['success'], assert_message)

    # ======================================================================

    def execute(self):
        response = self.get()
        self._test_get(response)

        response = self.post(self.user)
        self._test_post(response)

    # ======================================================================

    def test(self):
        assert_message = 'integration registration'
        pass
        # TODO

    # ======================================================================
