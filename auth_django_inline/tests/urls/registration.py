from django.test import TestCase
from django.urls import reverse, resolve

from ...settings import base_url, namespace, app_name


# Create your tests here.
class RegistrationTestCase(TestCase):
    base_url_expected = 'auth-django-inline/'
    namespace_expected = 'auth-django-inline'

    url_expected = '/' + base_url_expected + 'registration/'  # '/auth-django-inline/registration/'
    view_expected = namespace_expected + ':' + 'registration'   # 'auth-django-inline:registration'
    func_expected = app_name + '.' + 'views.registration.' + 'Registration'

    url = reverse(namespace + ':registration')
    view = resolve(url).view_name
    func = resolve(url)._func_path

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        # print('')
        # print('url_expected  ', self.url_expected)
        # print('url           ', self.url)
        # print('view_expected ', self.view_expected)
        # print('view          ', self.view)
        # print('func_expected ', self.func_expected)
        # print('func          ', self.func)
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def test_base_url(self):
        self.assertEquals(base_url, self.base_url_expected)

    def test_namespace(self):
        self.assertEquals(namespace, self.namespace_expected)

    def test_url(self):
        self.assertEquals(self.url, self.url_expected)

    def test_view(self):
        self.assertEquals(self.view, self.view_expected)

    def test_func(self):
        self.assertEquals(self.func, self.func_expected)

    # ======================================================================
