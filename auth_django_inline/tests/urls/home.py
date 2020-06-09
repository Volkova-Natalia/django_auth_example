from django.test import TestCase
from django.urls import reverse, resolve

from ...urls import base_url, namespace


# Create your tests here.
class HomeTestCase(TestCase):
    base_url_expected = 'auth-django-inline/'
    namespace_expected = 'auth-django-inline'

    url_expected = '/' + base_url_expected + ''  # '/auth-django-inline/'
    view_expected = namespace_expected + ':' + 'home'   # 'auth-django-inline:home'

    url = reverse(namespace + ':home')
    view = resolve(url).view_name

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

    # ======================================================================
