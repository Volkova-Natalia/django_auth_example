from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse

from ..forms import RegistrationForm


class Registration(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'auth_django_inline/registration.html',
                      {
                          'form': RegistrationForm,
                          'action': 'registration',
                      },
                      status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print('\nRegistration')
        print(request.data)
        form = RegistrationForm(request.data)
        if form.is_valid():
            form.save()
            return render(request,
                          'auth_django_inline/registration.html',
                          {
                            'form': form,
                            'action': 'registration',
                            'message': 'You successfully registered.'
                          },
                          status=status.HTTP_200_OK)
        else:
            return render(request,
                          'auth_django_inline/registration.html',
                          {
                              'form': form,
                              'action': 'registration',
                          },
                          status=status.HTTP_400_BAD_REQUEST)
