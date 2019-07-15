# -*- coding: UTF-8 -*-
from keywords.httpkeys1 import HTTP

http1 = HTTP()

# http1.seturl('http://47.101.197.102:8080/music/api/login')
http1.post('http://47.101.197.102:8080/music/api/login','username=admin&password=123456')
http1.savejson('result','id')
http1.get('http://47.101.197.102:8080/music/api/user','{id}')

