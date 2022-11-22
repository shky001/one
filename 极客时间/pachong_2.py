import urllib
import socket
from urllib import parse,request

data = bytes(parse.urlencode({1:'aaaaaaaaaaaaaa',2:'bbbbbbbbbbbbbbbbbb'}),encoding='utf-8')
print(data)                         # b'1=aaaaaaaaaaaaaa&2=bbbbbbbbbbbbbbbbbb'
# get请求
response1 = request.urlopen('http://httpbin.org/get',timeout=1)
print(response1.read())

# post请求
response2 = request.urlopen('http://httpbin.org/post',data=data,timeout=1)
print(response2.read().decode('utf-8'))

# 超时异常
try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT!")