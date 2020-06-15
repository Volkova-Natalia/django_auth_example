from .common import IntegrationCommonTestCase
from .registration import IntegrationRegistrationTestCase
from .login import IntegrationLoginTestCase
from .logout import IntegrationLogoutTestCase


# Create your tests here.
class IntegrationTestCase(IntegrationCommonTestCase):
    registration = IntegrationRegistrationTestCase()
    login = IntegrationLoginTestCase()
    logout = IntegrationLogoutTestCase()

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
        self.registration.execute(self.test_user)
        self.registration.test(self.test_user)

        self.login.execute(self.test_user)
        self.login.test(self.test_user)

        self.logout.execute(self.test_user)
        self.logout.test(self.test_user)

    # ======================================================================
    # dirty
    # ======================================================================

    # ======================================================================
