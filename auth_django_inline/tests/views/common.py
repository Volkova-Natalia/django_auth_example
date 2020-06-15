from django.test import TestCase
from django.test.client import Client


# Create your tests here.
class CommonTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def get(self, url=''):
        client = Client()
        response = client.get(url)
        return response

    def post(self, url='', data=None):
        client = Client()
        response = client.post(
            path=url,
            data=data,
            content_type='application/json'
        )
        return response

    # ======================================================================

    def _test_template(self, response, template_expected, assert_message=None):
        try:
            template = response.templates[0].name
        except:
            template = None
        self.assertEquals(template, template_expected, assert_message)

    def _test_form(self, response, form_expected, assert_message=None):
        try:
            form = response.context['form']
        except KeyError:
            form = None
        self.assertEquals(str(form), str(form_expected), assert_message)

    def _test_action(self, response, action_expected, assert_message=None):
        try:
            action = response.context['action']
        except KeyError:
            action = None
        self.assertEquals(action, action_expected, assert_message)

    def _test_message(self, response, message_expected, assert_message=None):
        try:
            message = response.context['message']
        except KeyError:
            message = None
        self.assertEquals(message, message_expected, assert_message)

    # ======================================================================
