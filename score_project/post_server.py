#!/usr/bin/env python
#coding=utf-8

import requests
import gameinfo
import sys
import json

BASE_URL = "http://127.0.0.1:8080/api/v1"
token="xxx"
Authorization = "token "+token
HEADER = {"Content-Type":"application/json","Authorization":Authorization}


def check_serverinfo_id():

    infourl = BASE_URL+"/serverinfo/"
    try:
        r = requests.get(infourl,headers=HEADER)
        for i in r.json():
            if i['internalip'] == gameinfo.INTERNAL_IP:
                return i['id']
        return None
    except Exception as e:
        print e

def check_serverinfo_exist_or_not():

    infourl = BASE_URL+"/serverinfo/"
    try:
        r = requests.get(infourl,headers=HEADER)
        for i in r.json():
            if i['internalip'] == gameinfo.INTERNAL_IP:
                return 1
        return 0
    except Exception as e:
        print e

def check_serverplugin_exist_or_not():
    id = check_serverinfo_id()
    infourl = BASE_URL+"/serverinfo/"+str(id)+"/serverplugin/"
    try:
        r = requests.get(infourl,headers=HEADER)
        if len(r.json()) == 0:
            return 0,None            
        id = r.json()[0]['id']
        return 1,str(id)
    except Exception as e:
        print e

def get_serverinfo():
    
    serverinfo = {}
    serverinfo['serverid'] = gameinfo.GID
    serverinfo['name'] = gameinfo.SERVER_NAME
    serverinfo['role'] = gameinfo.CODE_BRANCH
    serverinfo['internalip'] = gameinfo.INTERNAL_IP
    serverinfo['externalip'] = gameinfo.EXTERNAL_IP
    serverinfo['domain'] = gameinfo.DOMAIN
    serverinfo['status'] = gameinfo.STATUS
    serverinfo['gm'] = gameinfo.GM
    serverinfo['service'] = gameinfo.SERVICE
    return serverinfo

def get_serverplugin():

    serverplugin = {}
    f = open('my.cnf','r')
    mycnf = f.read()
    f.close()
    f = open('redis.conf','r')
    redisconf = f.read()
    f.close()
    f = open('php.ini','r')
    phpconf = f.read()
    f.close()
    php_status = 0
    redis_status = 1
    mysql_status = 0
    serverplugin['mysql_config'] = mycnf
    serverplugin['redis_config'] = redisconf
    serverplugin['php_config'] = phpconf
    serverplugin['php_status'] = php_status
    serverplugin['redis_status'] = redis_status
    serverplugin['mysql_status'] = mysql_status
    serverplugin['php_version'] = "7.1"
    serverplugin['redis_version'] = "3.2.8"
    serverplugin['mysql_version'] = "5.6"
    serverplugin['serverinfoid'] = check_serverinfo_id()
    return serverplugin

def commit_server(info):

    if info == "serverinfo":
        id = check_serverinfo_id()
        code = check_serverinfo_exist_or_not()
        post_url = BASE_URL+"/serverinfo/"
        server = get_serverinfo()
    #    put_url = BASE_URL+"/serverinfo/"+str(id)+"/"
        print server['serverid']
        put_url = BASE_URL+"/serverinfo/"+str(server['serverid'])+"/"

    if info == "serverplugin":
        code,id = check_serverplugin_exist_or_not()
        post_url = BASE_URL+"/serverplugin/"
        server = get_serverplugin()
        put_url = BASE_URL+"/serverplugin/"+str(id)+"/"

    try:
        if bool(code) == False:
            r = requests.post(post_url,data=json.dumps(server),headers=HEADER)
            print r.status_code
        if bool(code) == True:
            r = requests.put(put_url,data=json.dumps(server),headers=HEADER)
            print r.status_code
    except Exception as e:
        print e

if __name__ == "__main__":
    commit_server("serverinfo")
   # if gameinfo.SERVICE == "server":
   #     commit_server("serverplugin")
