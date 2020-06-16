from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse

from ...settings import namespace


# Create your tests here.
class HomeTestCase(TestCase):
    url = reverse(namespace + ':home')

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def test_get(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        template = response.templates[0].name
        template_expected = 'auth_django_inline/home.html'
        self.assertEquals(template, template_expected)

        request = response.context['request']
        response_content_expected = render(request, template_expected).content
        self.assertEquals(response.content, response_content_expected)

    # ======================================================================
