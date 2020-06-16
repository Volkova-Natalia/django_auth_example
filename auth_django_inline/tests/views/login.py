from django.test import TestCase

from .base.login import BaseLoginTestCase

from django.contrib.auth.models import User


# Create your tests here.
class LoginTestCase(TestCase):
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

    def test_get_clean(self):
        login = BaseLoginTestCase()
        client, response = login.get()
        login._test_get(response, success_fail='success', assert_message='views')

    # ----- POST -----

    def test_post_successful_clean(self):
        self._create_user(self.registered_user)
        data_post = self.registered_user.copy()

        login = BaseLoginTestCase(data_post)
        client, response = login.post()
        login._test_post(response, success_fail='success', assert_message='views')

    def test_post_user_is_not_correct_clean(self):
        self._create_user(self.registered_user)
        data_post = self.registered_user.copy()
        data_post['username'] = data_post['username'] + '_another'

        login = BaseLoginTestCase(data_post)
        client, response = login.post()
        login._test_post(response, success_fail='fail', assert_message='views')

    def test_post_password_is_not_correct_clean(self):
        self._create_user(self.registered_user)
        data_post = self.registered_user.copy()
        data_post['password'] = data_post['password'] + '_another'

        login = BaseLoginTestCase(data_post)
        client, response = login.post()
        login._test_post(response, success_fail='fail', assert_message='views')

    def test_post_user_password_is_not_correct_clean(self):
        self._create_user(self.registered_user)
        data_post = self.registered_user.copy()
        data_post['username'] = data_post['username'] + '_another'
        data_post['password'] = data_post['password'] + '_another'

        login = BaseLoginTestCase(data_post)
        client, response = login.post()
        login._test_post(response, success_fail='fail', assert_message='views')

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
