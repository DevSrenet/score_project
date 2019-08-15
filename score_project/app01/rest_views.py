#!/usr/bin/env python
#coding=utf-8
#from django.contrib.auth.models import User
from rest_framework import routers,viewsets,filters
from app01.models import *
from serializers import *
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import detail_route

class BaseInfoViewSet(viewsets.ModelViewSet):
    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer

class ServerInfoViewSet(viewsets.ModelViewSet):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer
    lookup_field = 'serverid'


    @detail_route(methods=['get','post'], permission_classes=[permissions.AllowAny],url_path='serverplugin')
    def serverplugin(self,request,*args,**kwargs):
    	if request.method == "GET":
    		res = ServerPlugin.objects.filter(server__id=self.kwargs['serverid'])
    		serializer = ServerPluginSerializer(res,many = True)
    		return Response(serializer.data)



class ServerPluginViewSet(viewsets.ModelViewSet):
    queryset = ServerPlugin.objects.all()
    serializer_class = ServerPluginSerializer

    def create(self,request):
    	id = request.data['serverinfoid']
    	serverinfo = ServerInfo.objects.get(id=id)
    	p = ServerPlugin(server=serverinfo,mysql_config=request.data['mysql_config'],redis_config=request.data['redis_config'],
    		php_config=request.data['php_config'],mysql_status=request.data['mysql_status'],php_status=request.data['php_status'],
    		redis_status=request.data['redis_status'],mysql_version=request.data['mysql_version'],
    		php_version=request.data['php_version'],redis_version=request.data['redis_version'])
    	p.save()
    	return Response(status=status.HTTP_201_CREATED)
