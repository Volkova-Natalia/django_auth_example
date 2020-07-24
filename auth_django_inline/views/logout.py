from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse

from django.contrib.auth import logout
from ..settings import base_url, end_point


decorators = [login_required(login_url='/' + base_url + end_point['login']['url'])]


@method_decorator(decorators, name='dispatch')
class Logout(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'auth_django_inline/logout.html',
                      {
                          'action': 'logout',
                      },
                      status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print('\nLogout')
        print(request.data)
        print(request.COOKIES)
        logout(request)
        return render(request,
                      'auth_django_inline/logout.html',
                      {
                          'action': 'logout',
                          'message': 'You successfully logged out.'
                      },
                      status=status.HTTP_200_OK)
