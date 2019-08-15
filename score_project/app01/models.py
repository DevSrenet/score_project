#coding=utf-8
from django.db import models
#from app01.account_models import Account
# Create your models here.

class BaseInfo(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.title

class ServerInfo(models.Model):
    serverid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    internalip = models.GenericIPAddressField(u'内网ip', blank=True, null=True)
    externalip = models.GenericIPAddressField(u'外网ip', blank=True, null=True)
    domain = models.CharField(max_length=120, blank=True, null=True)
    gm = models.CharField(max_length=100, blank=True, null=True)
    service = models.CharField(max_length=100, blank=True, null=True)
    terminal = models.CharField(max_length=300, blank=True, null=True)

    status_choices = (
            (0,'在线'),
            (1,'离线'),
            (2,'正常'),
        )
    status = models.SmallIntegerField(choices=status_choices,default=1)

    def __unicode__(self):
        return str(self.serverid)+"-"+self.name


class ServerPlugin(models.Model):
    server = models.ForeignKey(ServerInfo,blank=True, null=True,on_delete=models.CASCADE)
    mysql_config = models.TextField(max_length=5000, blank=True, null=True)
    php_config = models.TextField(max_length=5000, blank=True, null=True)
    redis_config = models.TextField(max_length=5000, blank=True, null=True)
    status_choices = (
            (0,'running'),
            (1,'down'),
        )
    mysql_status = models.SmallIntegerField(choices=status_choices,default=1)
    php_status = models.SmallIntegerField(choices=status_choices,default=1)
    redis_status = models.SmallIntegerField(choices=status_choices,default=1)
    mysql_version = models.CharField(max_length=30, blank=True, null=True)
    redis_version = models.CharField(max_length=30, blank=True, null=True)
    php_version = models.CharField(max_length=30, blank=True, null=True)
    

    def __unicode__(self):
        return str(self.server.serverid)

class DockerInfo(models.Model):
    server = models.ForeignKey(ServerInfo,blank=True, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    terminal = models.CharField(max_length=300, blank=True, null=True)
    status = models.BooleanField(default=1)

    def __unicode__(self):
        return str(self.server.serverid)+"-"+self.name
