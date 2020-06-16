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
    # clean
    # ======================================================================

    # ----- GET -----

    def test_get_clean(self):
        registration = BaseRegistrationTestCase()
        response = registration.get()
        registration._test_get(response, success_fail='success', assert_message='views')

    # ----- POST -----

    def test_post_successful_clean(self):
        self._create_user(self.registered_user)

        data_post = self.registered_user.copy()
        data_post['username'] = data_post['username'] + '_another'
        data_post['password'] = data_post['password'] + '_another'

        registration = BaseRegistrationTestCase(data_post)
        response = registration.post()
        registration._test_post(response, success_fail='success', assert_message='views')

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

    def test_post_user_exists_clean(self):
        self._create_user(self.registered_user)

        data_post = self.registered_user.copy()
        data_post['password'] = data_post['password'] + '_another'

        registration = BaseRegistrationTestCase(data_post)
        response = registration.post()
        registration._test_post(response, success_fail='fail', assert_message='views')

        count_users_expected = 1
        count_users = User.objects.count()
        self.assertEquals(count_users, count_users_expected)

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
