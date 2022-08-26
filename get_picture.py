import xlrd        # 读取excel文件需要的库
import requests
from bs4 import BeautifulSoup
import urllib.request

# 打开文件
data = xlrd.open_workbook("2022年CMS资讯-获取图片.xlsx")
table = data.sheets()[0]  # 表头，第几个sheet表-1
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.col_values(4)  # url列数据
# print(type(colnames),colnames)

x = 1    # 记录总下载次数
# for num in range(1,3):
for num in range(1,len(colnames)):
    a=1
    url = colnames[num]
    # print(url)
    picurl_start = url[:-22]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    req = requests.get(url,headers=headers)  # Get方式获取网页数据
    req.encoding = 'utf-8'
    html = req.text           #获取网站数据
    soup = BeautifulSoup(html, 'html.parser')       # 解析网页
    imgs = soup.find_all('img')        # 获取所有的img标签
    for i in imgs:
        # print("img标签===  ",i)
        imgsrc = i.get('oldsrc')
        if imgsrc:
            # print("图片名imgsrc:  ",imgsrc)
            picurl = picurl_start + imgsrc
            # print(picurl)

            # 本地路径
            filename = 'C:\\Users\\31872\\Desktop\\001\\picture\\%s' % imgsrc
            # 将URL表示的网络对象复制到本地文件
            urllib.request.urlretrieve(picurl, filename)
            print('下载第%d张' % x)
            a+=1
            x += 1
    print('****** 本次下载完成! ******')
print("共下载图片数： ",x)
