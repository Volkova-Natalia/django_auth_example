"""auth_django_inline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .settings import app_name, end_point
from . import views


app_name = app_name
urlpatterns = [
    path('', views.home, name='home'),

    path(end_point['registration']['url'], views.Registration.as_view(), name=end_point['registration']['name']),
    path(end_point['login']['url'], views.Login.as_view(), name=end_point['login']['name']),
    path(end_point['logout']['url'], views.Logout.as_view(), name=end_point['logout']['name']),
]
