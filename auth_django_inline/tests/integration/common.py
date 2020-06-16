# from ..views.common import CommonTestCase
#
#
# # Create your tests here.
# class IntegrationCommonTestCase(CommonTestCase):
#     url = None
#
#     status_code_expected = {
#         'get': None,
#         'post': {
#             'success': None,
#             'fail': None,
#         }
#     }
#
#     template_expected = None
#
#     form_expected = {
#         'get': None,
#         'post': None,
#     }
#
#     form_valid_expected = {
#         'get': None,
#         'post': None,
#     }
#
#     action_expected = None
#
#     message_expected = {
#         'get': None,
#         'post': {
#             'success': None,
#             'fail': None,
#         }
#     }
#
#     # ======================================================================
#
#     def __init__(self, user=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#
#     # ======================================================================
#
#     @classmethod
#     def setUpTestData(cls):
#         pass
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     # ======================================================================
#
#     def get(self):
#         response = super().get(self.url)
#         return response
#
#     def post(self, user=None):
#         response = super().post(self.url, user)
#         return response
#
#     # ======================================================================
#
#     def _test_get(self, response, assert_message=''):
#         self.assertEquals(response.status_code,
#                           self.status_code_expected['get'],
#                           assert_message + ' test status_code')
#         self._test_template(response, self.template_expected, assert_message + ' test template')
#         self._test_form(response, self.form_expected['get'], assert_message + ' test form')
#         self._test_action(response, self.action_expected, assert_message + ' test action')
#         self._test_message(response, self.message_expected['get'], assert_message + ' test message')
#
#     def _test_post(self, response, assert_message=''):
#         self.assertEquals(response.status_code,
#                           self.status_code_expected['post']['success'],
#                           assert_message + ' test status_code')
#         self._test_template(response, self.template_expected, assert_message + ' test template')
#         self.assertEquals(self.form_valid_expected['post'], True, assert_message + ' test form_valid')
#         self._test_form(response, self.form_expected['post'], assert_message + ' test form')
#         self._test_action(response, self.action_expected, assert_message + ' test action')
#         self._test_message(response, self.message_expected['post']['success'], assert_message + ' test message')
#
#     # ======================================================================
