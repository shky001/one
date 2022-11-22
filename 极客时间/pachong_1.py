from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://httpbin.org.com'
response = request.urlopen(url)
print(response.read().decode('utf_8'))