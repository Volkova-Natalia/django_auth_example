from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse

from ...urls import namespace


# Create your tests here.
class RegisterTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    # ======================================================================
