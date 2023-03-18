import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        # r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print (r.content)
        return r.text
    except:
        return "失败"

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # print (soup)
    for tr in soup.find('tbody').children:
        # print (tr)
        # print ('===================')
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            # print (tds[0])
            # print('===================')
            # ulist.append([tds[0], tds[1], tds[2]])
            ulist.append([tds[0].get_text().strip(), tds[1].get_text().strip(), tds[2].get_text().strip()])
            # ulist.append([tds[0].get_text(), tds[1].get_text(), tds[2].get_text()])

def printUnivList(ulist, num):
    print("{:^1}\t{:^1}\t{:^8}".format("排名", "学校名称", "地区"))
    for i in range(num):
        u = ulist[i]
        # print (u)
        print("{:^1}\t{:^1}\t{:^8}".format(u[0], u[1],u[2]))

def main():
    unifo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)  # 20 univs

main()