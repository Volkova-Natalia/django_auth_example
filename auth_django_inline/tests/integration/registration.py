from rest_framework import status
from django.urls import reverse

from .common import IntegrationCommonTestCase

from ...urls import namespace
from ...forms import RegistrationForm


# Create your tests here.
class IntegrationRegistrationTestCase(IntegrationCommonTestCase):
    url = reverse(namespace + ':registration')

    status_code_expected = {
        'get': status.HTTP_200_OK,
        'post': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        }
    }

    template_expected = 'auth_django_inline/registration.html'

    form_expected = {
        'get': RegistrationForm,
        'post': RegistrationForm,
    }

    form_valid_expected = {
        'get': None,
        'post': None,
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
        super().__init__(user=user, *args, **kwargs)
        self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_valid_expected['post'] = self.form_expected['post'].is_valid()

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
        assert_message = 'integration registration GET'
        super()._test_get(response, assert_message)

    def _test_post(self, response):
        assert_message = 'integration registration POST'
        super()._test_post(response, assert_message)

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
