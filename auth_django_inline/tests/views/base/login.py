from rest_framework import status
from django.urls import reverse
from django.contrib.auth import authenticate

from ..common import CommonTestCase

from ....urls import namespace
from ....forms import LoginForm


# Create your tests here.
class BaseLoginTestCase(CommonTestCase):
    url = reverse(namespace + ':login')

    status_code_expected = {
        'get': status.HTTP_200_OK,
        'post': {
            'success': status.HTTP_200_OK,
            'fail': None,   # TODO
        }
    }

    template_expected = 'auth_django_inline/login.html'

    form_expected = {
        'get': LoginForm,
        'post': LoginForm,
    }

    form_valid_expected = {
        'get': None,
        'post': None,
    }

    action_expected = 'login'

    message_expected = {
        'get': None,
        'post': {
            'success': 'You successfully logged.',
            'fail': None,
        }
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

    def get(self):
        response = super().get(self.url)
        return response

    # def post(self, user=None):
    def post(self):
        # response = super().post(self.url, user)
        response = super().post(self.url, self.user)
        return response

    # ======================================================================

    def _test_get(self, response, assert_message=''):
        assert_message = assert_message + ' login GET'
        super()._test_get(response, assert_message)

    def _test_post(self, response, assert_message=''):
        assert_message = assert_message + ' login POST'
        # self.form_expected['post'] = self.form_expected['post'](self.user)
        self.form_expected['post'] = LoginForm(self.user)
        self.form_valid_expected['post'] = self.form_expected['post'].is_valid()
        super()._test_post(response, assert_message)

        user = authenticate(username=self.user['username'], password=self.user['password'])
        self.assertNotEquals(user, None, assert_message + ' test user')
        self.assertEquals(user.is_active, True, assert_message + ' test user.is_active')

    # ======================================================================
