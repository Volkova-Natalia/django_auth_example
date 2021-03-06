from django.test import TestCase
from django.test.client import Client


# Create your tests here.
class CommonTestCase(TestCase):
    url = None

    status_code_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    template_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    form_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    form_expected_valid = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    form_expected_valid_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    action_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    message_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    # ======================================================================

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def get(self, client=None, url=''):
        if not client:
            client = Client()
        response = client.get(url)
        return client, response

    def post(self, client=None, url='', data=None):
        if not client:
            client = Client()
        response = client.post(
            path=url,
            data=data,
            content_type='application/json'
        )
        return client, response

    def client_login(self, client=None, user={'username': '', 'password': ''}):
        if not client:
            client = Client()
        login = client.login(username=user['username'], password=user['password'])
        return client, login

    def client_logout(self, client=None, user={'username': '', 'password': ''}):
        if not client:
            client = Client()
        logout = client.logout()
        return client, logout

    # ======================================================================

    def _test_template(self, response, template_expected, assert_message=None):
        try:
            template = response.templates[0].name
        except (AttributeError, NameError, TypeError, ValueError, Exception):
            template = None
        self.assertEquals(template, template_expected, assert_message)

    def _test_form(self, response, form_expected, assert_message=None):
        try:
            form = response.context['form']
        except (AttributeError, NameError, TypeError, ValueError, Exception):
            form = None
        self.assertEquals(str(form), str(form_expected), assert_message)

    def _test_action(self, response, action_expected, assert_message=None):
        try:
            action = response.context['action']
        except (AttributeError, NameError, TypeError, ValueError, Exception):
            action = None
        self.assertEquals(action, action_expected, assert_message)

    def _test_message(self, response, message_expected, assert_message=None):
        try:
            message = response.context['message']
        except (AttributeError, NameError, TypeError, ValueError, Exception):
            message = None
        self.assertEquals(message, message_expected, assert_message)

    # ======================================================================

    def _test_get(self, response, success_fail, assert_message=''):
        self.assertEquals(response.status_code,
                          self.status_code_expected['get'][success_fail],
                          assert_message + ' test status_code')

        self._test_template(response,
                            self.template_expected['get'][success_fail],
                            assert_message + ' test template')

        self._test_form(response,
                        self.form_expected['get'][success_fail],
                        assert_message + ' test form')

        self._test_action(response,
                          self.action_expected['get'][success_fail],
                          assert_message + ' test action')

        self._test_message(response,
                           self.message_expected['get'][success_fail],
                           assert_message + ' test message')

    def _test_post(self, response, success_fail, assert_message=''):
        self.assertEquals(response.status_code,
                          self.status_code_expected['post'][success_fail],
                          assert_message + ' test status_code')

        self._test_template(response,
                            self.template_expected['post'][success_fail],
                            assert_message + ' test template')

        self.assertEquals(self.form_expected_valid['post'][success_fail],
                          self.form_expected_valid_expected['post'][success_fail],
                          assert_message + ' test form_valid')

        self._test_form(response,
                        self.form_expected['post'][success_fail],
                        assert_message + ' test form')

        self._test_action(response,
                          self.action_expected['post'][success_fail],
                          assert_message + ' test action')

        self._test_message(response,
                           self.message_expected['post'][success_fail],
                           assert_message + ' test message')

    # ======================================================================
