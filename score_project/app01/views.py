#coding=utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.shortcuts import render_to_response,render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import auth
from app01.models import *
from rest_framework_jwt.settings import api_settings
from django.conf import settings
import json

def get_serverlist():
	filename = settings.SERVERLIST
	with open(filename,'r') as f:
		info = json.load(f)
	f.close()
	return info

def set_cookie_header(request):
	user = request.user
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)
	return token

@login_required
def index(request):
	token = set_cookie_header(request)
	baseinfo = BaseInfo.objects.all()
	response = render_to_response('baseinfo.html',locals())
	response.set_cookie('Token',token)
	return response

@login_required
def server(request):
	serverinfo = ServerInfo.objects.order_by('serverid')
	serverplugin = ServerPlugin.objects.all()
	dockerinfo = DockerInfo.objects.all()
	response = render_to_response('server.html',locals())
	return response

@login_required
def serverlist(request):
	listinfo = get_serverlist()
	response = render_to_response('serverlist.html',locals())
	return response