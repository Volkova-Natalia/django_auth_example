from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse

from .common import CommonTestCase

from ...urls import namespace
from ...forms import RegistrationForm
from django.contrib.auth.models import User


# Create your tests here.
class RegistrationTestCase(CommonTestCase):
    url = reverse(namespace + ':registration')

    registered_user = {
        'username': 'username_000',
        'password': 'password_000',
    }

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    # ======================================================================
    # clean
    # ======================================================================

    # ----- GET -----

    def test_get_clean(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self._test_template(response, 'auth_django_inline/registration.html')
        self._test_form(response, RegistrationForm)
        self._test_action(response, 'registration')
        self._test_message(response, None)

    # ----- POST -----

    def _post(self, data_post=registered_user.copy()):
        user = User.objects.create_user(
            username=self.registered_user['username'],
            password=self.registered_user['password'],
        )
        user.save()

        form_expected = RegistrationForm(data_post)
        form_valid_expected = form_expected.is_valid()

        client = Client()
        response = client.post(
            path=self.url,
            data=data_post,
            content_type='application/json'
        )
        return response, form_expected, form_valid_expected

    def test_post_successful_registration_clean(self):
        data_post = self.registered_user.copy()
        data_post['username'] = data_post['username'] + '_another'
        data_post['password'] = data_post['password'] + '_another'
        response, form_expected, form_valid_expected = self._post(data_post)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self._test_template(response, 'auth_django_inline/registration.html')
        self.assertEquals(form_valid_expected, True)
        self._test_form(response, form_expected)
        self._test_action(response, 'registration')
        self._test_message(response, 'You successfully registered.')

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
        data_post = self.registered_user.copy()
        data_post['password'] = data_post['password'] + '_another'
        response, form_expected, form_valid_expected = self._post(data_post)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        self._test_template(response, 'auth_django_inline/registration.html')
        self.assertEquals(form_valid_expected, False)
        self._test_form(response, form_expected)
        self._test_action(response, 'registration')
        self._test_message(response, None)

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
