from django.test import TestCase

from .base.logout import BaseLogoutTestCase

from django.contrib.auth.models import User


# Create your tests here.
class LogoutTestCase(TestCase):
    registered_user = {
        'username': 'username_000',
        'password': 'password_000',
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

    def _create_user(self, user=registered_user.copy()):
        user = User.objects.create_user(
            username=user['username'],
            password=user['password'],
        )
        user.save()

    # ======================================================================
    # success
    # ======================================================================

    # ----- GET -----

    def test_get_success(self):
        success_fail = 'success'

        self._create_user(self.registered_user)
        logout = BaseLogoutTestCase()
        client, client_login = logout.client_login(client=None, user=self.registered_user)
        client, response = logout.get(client=client)
        logout._test_get(response, success_fail=success_fail, assert_message='views')

    # ----- POST -----

    def test_post_success(self):
        success_fail = 'success'

        self._create_user(user=self.registered_user)
        logout = BaseLogoutTestCase(user=self.registered_user)
        client, client_login = logout.client_login(client=None, user=self.registered_user)
        client, response = logout.post(client=client)
        client, client_logout = logout.client_logout(client=None, user=self.registered_user)
        logout._test_post(response, success_fail=success_fail, assert_message='views')

    # ======================================================================
    # fail
    # ======================================================================

    # ----- GET -----

    def test_get_login_required_fail(self):
        success_fail = 'fail'

        logout = BaseLogoutTestCase()
        client, response = logout.get(client=None)
        logout._test_get(response, success_fail=success_fail, assert_message='views')

    # ----- POST -----

    def test_post_login_required_fail(self):
        success_fail = 'fail'

        logout = BaseLogoutTestCase(user=self.registered_user)
        client, response = logout.post(client=None)
        logout._test_post(response, success_fail=success_fail, assert_message='views')

    # ======================================================================
