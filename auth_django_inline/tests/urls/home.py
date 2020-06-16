from django.test import TestCase
from django.urls import reverse, resolve

from ...settings import base_url, namespace, app_name


# Create your tests here.
class HomeTestCase(TestCase):
    base_url_expected = 'auth-django-inline/'
    namespace_expected = 'auth-django-inline'

    url_expected = '/' + base_url_expected + ''  # '/auth-django-inline/'
    view_expected = namespace_expected + ':' + 'home'   # 'auth-django-inline:home'
    func_expected = app_name + '.' + 'views.home.' + 'home'

    url = reverse(namespace + ':home')
    view = resolve(url).view_name
    func = resolve(url)._func_path

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
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
