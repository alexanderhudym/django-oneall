# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^login', views.oa_login, name='oneall-login'),
    url('^logout', views.oa_logout, name='oneall-logout'),
    url('^profile', views.oa_profile, name='oneall-profile'),
    url('^nosocial', views.oa_nosocial, name='oneall-nosocial')
]
