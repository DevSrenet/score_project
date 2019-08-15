#!/usr/bin/env python

from django.conf.urls import url, include
from rest_framework import routers, viewsets
from serializers import *
import rest_views
from app01.views import *

router = routers.DefaultRouter()
router.register(r'baseinfo',rest_views.BaseInfoViewSet)
router.register(r'serverinfo',rest_views.ServerInfoViewSet)
router.register(r'serverplugin',rest_views.ServerPluginViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
   # url(r'^api-auth/login/$',login),
    #url(r'^api-auth/logout/$',logout),
   # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
