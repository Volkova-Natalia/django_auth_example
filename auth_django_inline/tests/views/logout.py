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
    # clean
    # ======================================================================

    # ----- GET -----

    def test_get_successful_clean(self):
        self._create_user(self.registered_user)
        logout = BaseLogoutTestCase()
        client, client_login = logout.client_login(client=None, user=self.registered_user)
        client, response = logout.get(client=client)
        logout._test_get(response, success_fail='success', assert_message='views')

    def test_get_login_required_clean(self):
        logout = BaseLogoutTestCase()
        client, response = logout.get(client=None)
        logout._test_get(response, success_fail='fail', assert_message='views')

    # ----- POST -----

    # ======================================================================
    # dirty
    # ======================================================================

    # ----- GET -----

    def test_get_dirty(self):
        pass

    # ----- POST -----

    def test_post_dirty(self):
        pass

    # ======================================================================
