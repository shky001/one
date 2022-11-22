import requests

# get请求
url = 'http://httpbin.org/get'
data = {111:'AAAAAAAAAAA',222:'BBBBBBBBBBBBBBB'}
response = requests.get(url,data)
# print(response.text)

# post请求
url = 'http://httpbin.org/post'
data = {111:'qwerasdf',222:'uiophjkl'}
response = requests.post(url,data)
print(response.text)