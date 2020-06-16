from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse

from ..forms import LoginForm


class Login(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'auth_django_inline/login.html',
                      {
                          'form': LoginForm,
                          'action': 'login',
                      },
                      status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print('\nLogin')
        print(request.data)
        form = LoginForm(request.data)
        if form.is_valid():
            form.login(request)
            return render(request,
                          'auth_django_inline/login.html',
                          {
                              'form': form,
                              'action': 'login',
                              'message': 'You successfully logged in.'
                          },
                          status=status.HTTP_200_OK)
        else:
            return render(request,
                          'auth_django_inline/login.html',
                          {
                              'form': form,
                              'action': 'login',
                          },
                          status=status.HTTP_400_BAD_REQUEST)
