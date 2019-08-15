#!/usr/bin/env python
from rest_framework import serializers
from app01.models import *


class ServerPluginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerPlugin
        fields = ('id','mysql_config','php_config','redis_config','mysql_status','php_status','redis_status','mysql_version','redis_version','php_version')

class ServerInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('id','serverid','name','role','version','internalip','externalip','domain','status','gm','service')

class BaseInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseInfo
        fields = ('id',"title",'content')
