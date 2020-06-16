from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse

from .common import CommonTestCase
from .base.login import BaseLoginTestCase

from ...urls import namespace
from ...forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your tests here.
class LoginTestCase(TestCase):
    # url = reverse(namespace + ':login')

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
        response = login.get()
        login._test_get(response, assert_message='views')

    # ----- POST -----
    #
    # def _post(self, data_post=registered_user.copy()):
    #     user = User.objects.create_user(
    #         username=self.registered_user['username'],
    #         password=self.registered_user['password'],
    #     )
    #     user.save()
    #     client = Client()
    #     response = client.post(
    #         path=self.url,
    #         data=data_post,
    #         content_type='application/json'
    #     )
    #     return response
    #
    # def _test_post_successful_login(self, response, data_post):
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #
    #     self._test_template(response, 'auth_django_inline/login.html')
    #     form_expected = LoginForm(data_post)
    #     form_valid_expected = form_expected.is_valid()
    #     self.assertEquals(form_valid_expected, True)
    #     self._test_form(response, form_expected)
    #     self._test_action(response, 'login')
    #     self._test_message(response, 'You successfully logged.')
    #
    #     user = authenticate(username=data_post['username'], password=data_post['password'])
    #     self.assertNotEquals(user, None)
    #     self.assertEquals(user.is_active, True)
    #
    # def _test_post_failed_login(self, response, data_post):
    #     self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
    #
    #     self._test_template(response, 'auth_django_inline/login.html')
    #     form_expected = LoginForm(data_post)
    #     form_valid_expected = form_expected.is_valid()
    #     self.assertEquals(form_valid_expected, False)
    #     self._test_form(response, form_expected)
    #     self._test_action(response, 'login')
    #     self._test_message(response, None)
    #
    #     user = authenticate(username=data_post['username'], password=data_post['password'])
    #     self.assertEquals(user, None)

    def test_post_successful_clean(self):
        self._create_user(self.registered_user)
        data_post = self.registered_user.copy()
        login = BaseLoginTestCase(data_post)
        response = login.post()
        login._test_post(response, assert_message='views')

    # def test_post_user_is_not_correct_clean(self):
    #     data_post = self.registered_user.copy()
    #     data_post['username'] = data_post['username'] + '_another'
    #     response = self._post(data_post)
    #     self._test_post_failed_login(response, data_post)
    #
    # def test_post_password_is_not_correct_clean(self):
    #     data_post = self.registered_user.copy()
    #     data_post['password'] = data_post['password'] + '_another'
    #     response = self._post(data_post)
    #     self._test_post_failed_login(response, data_post)
    #
    # def test_post_user_password_is_not_correct_clean(self):
    #     data_post = self.registered_user.copy()
    #     data_post['username'] = data_post['username'] + '_another'
    #     data_post['password'] = data_post['password'] + '_another'
    #     response = self._post(data_post)
    #     self._test_post_failed_login(response, data_post)
    #
    # # ======================================================================
    # # dirty
    # # ======================================================================
    #
    # # ----- GET -----
    #
    # def test_get_dirty(self):
    #     pass
    #
    # # ----- POST -----
    #
    # def test_post_dirty(self):
    #     pass
    #
    # # ======================================================================
