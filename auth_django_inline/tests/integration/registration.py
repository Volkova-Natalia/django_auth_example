from rest_framework import status
from django.urls import reverse

from ..views.base.registration import BaseRegistrationTestCase

from ...urls import namespace
from ...forms import RegistrationForm


# Create your tests here.
class IntegrationRegistrationTestCase(BaseRegistrationTestCase):

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def execute(self):
        response = self.get()
        self._test_get(response, assert_message='integration')

        # response = self.post(self.user)
        response = self.post()
        self._test_post(response, assert_message='integration')

    # ======================================================================

    def test(self):
        assert_message = 'integration registration'
        pass
        # TODO

    # ======================================================================
