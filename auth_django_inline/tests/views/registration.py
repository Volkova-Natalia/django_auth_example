from django.test import TestCase

from .base.registration import BaseRegistrationTestCase

from django.contrib.auth.models import User


# Create your tests here.
class RegistrationTestCase(TestCase):
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

        registration = BaseRegistrationTestCase()
        client, response = registration.get(client=None)
        registration._test_get(response, success_fail=success_fail, assert_message='views')

    # ----- POST -----

    def test_post_success(self):
        success_fail = 'success'

        self._create_user(self.registered_user)

        data_post = self.registered_user.copy()
        data_post['username'] = data_post['username'] + '_another'
        data_post['password'] = data_post['password'] + '_another'

        registration = BaseRegistrationTestCase(data_post)
        client, response = registration.post(client=None)
        registration._test_post(response, success_fail=success_fail, assert_message='views')

        count_users_expected = 2
        count_users = User.objects.count()
        self.assertEquals(count_users, count_users_expected)

        user = User.objects.get(id=count_users)
        for field in data_post.keys():
            if field != 'password':
                self.assertEquals(getattr(user, field), data_post[field])
            else:
                self.assertNotEquals(getattr(user, field), data_post[field])
                self.assertEquals(user.check_password(data_post[field]), True)

    # ======================================================================
    # fail
    # ======================================================================

    # ----- GET -----

    def test_get_fail(self):
        pass

    # ----- POST -----

    def test_post_user_exists_fail(self):
        success_fail = 'fail'

        self._create_user(self.registered_user)

        data_post = self.registered_user.copy()
        data_post['password'] = data_post['password'] + '_another'

        registration = BaseRegistrationTestCase(data_post)
        client, response = registration.post(client=None)
        registration._test_post(response, success_fail=success_fail, assert_message='views')

        count_users_expected = 1
        count_users = User.objects.count()
        self.assertEquals(count_users, count_users_expected)

    # ======================================================================
