from django.test import TestCase


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

    def _test_template(self, response, template_expected):
        try:
            template = response.templates[0].name
        except:
            template = None
        self.assertEquals(template, template_expected)

    def _test_form(self, response, form_expected):
        try:
            form = response.context['form']
        except KeyError:
            form = None
        self.assertEquals(str(form), str(form_expected))

    def _test_action(self, response, action_expected):
        try:
            action = response.context['action']
        except KeyError:
            action = None
        self.assertEquals(action, action_expected)

    def _test_message(self, response, message_expected):
        try:
            message = response.context['message']
        except KeyError:
            message = None
        self.assertEquals(message, message_expected)

    # ======================================================================
