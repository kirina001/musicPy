# -*- coding: UTF-8 -*-
from keywords.httpkeys1 import HTTP

http1 = HTTP()

# http1.seturl('http://47.101.197.102:8080/music/api/login')
# http1.post('http://47.101.197.102:8080/music/api/login','username=admin&password=123456')
# http1.savejson('result','id')
# http1.get('http://47.101.197.102:8080/music/api/user','{id}')

data = {'username':'admin','password':'123456'}
# json方式传递数据
http1.postjson('http://47.101.197.102:8080/music/api/login',data=data)
http1.savejson('result','id')
http1.get('http://47.101.197.102:8080/music/api/user','{id}')


