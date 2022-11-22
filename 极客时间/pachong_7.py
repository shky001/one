# 使用爬虫爬取新闻网站

import requests
from bs4 import BeautifulSoup

url = "https://www.infoq.cn/news"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

# 获取新闻标题
def get_newsTitles(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    for title_href in soup.find_all('div', class_='items__content'):
        print("*******")
        print([title.get('title')
              for title in title_href.find_all('a') if title.get('title')])

# 翻页
for i in range(15, 46, 15):
    url = 'http://www.infoq.cn/news/' + str(i)
    # print(url)
    get_newsTitles(url)