from bs4 import BeautifulSoup
import requests
import os
import shutil

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "close",
    "Cookie": "_gid=GA1.2.1117128164.1669117353; JSESSIONID=84FE1C86EEF78C673619D32097092ACD; AWSALB=iQJRugFZFNKJCPGTR+Y9rLGhl1Lii+tnoe9scf83y1W4SFyyhxa3sIh5HnYImteW6/zjQVhpmTaS3loiuSkxaJ3n514isKSQUqmL2aIV4rkon8/udkSLKG1/4jHh; AWSALBCORS=iQJRugFZFNKJCPGTR+Y9rLGhl1Lii+tnoe9scf83y1W4SFyyhxa3sIh5HnYImteW6/zjQVhpmTaS3loiuSkxaJ3n514isKSQUqmL2aIV4rkon8/udkSLKG1/4jHh; _ga_VMVPD4D2JY=GS1.1.1669208081.4.1.1669209609.0.0.0; _ga=GA1.1.1499213446.1669117353",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36 Edg/103.0.1264.77"
}

url = 'http://www.infoq.com/cn/presentations'


# 下载图片
def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)


# 获取图片
def get_Picture(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print("000")
    print(soup)
    for pic_href in soup.find_all('ul'):
        print("1111111")
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            print("************",imgurl)
            dir = os.path.abspath('.')
            filename = os.path.basename(imgurl)
            imgpath = os.path.join(dir, filename)
            print('开始下载 %s' % imgurl)
            download_jpg(imgurl, imgpath)


get_Picture(url)

# 翻页
j = 0
for i in range(12, 37, 12):
    url = 'http://www.infoq.com/presentations' + str(i)
    j += 1
    print('第 %d 页' % j)
    get_Picture(url)
