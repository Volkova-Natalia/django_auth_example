from django.test import TestCase

from .registration import IntegrationRegistrationTestCase
from .login import IntegrationLoginTestCase
from .logout import IntegrationLogoutTestCase


# Create your tests here.
class IntegrationTestCase(TestCase):
    test_user = {
        'username': 'username_test',
        'password': 'password_test',
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
    # clean
    # ======================================================================

    def test_registration_login_logout_clean(self):
        registration = IntegrationRegistrationTestCase(user=self.test_user)
        login = IntegrationLoginTestCase(user=self.test_user)
        logout = IntegrationLogoutTestCase(user=self.test_user)

        registration.execute()
        registration.test()

        login.execute()
        login.test()

        logout.execute()
        logout.test()

    # ======================================================================
    # dirty
    # ======================================================================

    # ======================================================================
