import requests
import json

import pymysql
import pymysql as mysql


# 连接数据库
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='pachong',
    charset='utf8',
)
cursor = conn.cursor()
print("连接成功")

def pachong(url,page):
    req = requests.get(url)  # Get方式获取网页数据
    req.encoding = 'utf-8'
    s1 = req.text.strip()  # 去除两边空字符
    texts = s1.strip('()')  # 去除括号()
    # print(texts)
    # print("类型： ",type(texts))

    # 解析数据
    dict_data = json.loads(texts)  # 转换格式
    # print(type(dict_data))     # <class 'dict'>
    # print(dict_data)
    count_page = dict_data['pages']
    # count_xunhuan = 1
    print(page,count_page)
    while int(page) <= count_page:
        result_list = dict_data['results']
        # print(type(result_list))    # <class 'list'>
        # print(result_list)
        data_list = []  # 创建空列表
        # 获取results结果 列表数据
        i = 1
        for result in result_list:
            # print(type(result))
            doctitle = result['doctitle']
            docpubtime = result['docpubtime']
            dockeywords = result['dockeywords']
            docpuburl = result['docpuburl']
            docabstract = result['docabstract']
            docreltime = result['docreltime']
            subdoctitle = result['subdoctitle']
            imgsrc = result['imgsrc']
            docauthor = result['docauthor']
            # print(type(result),result)
            # print("result['docauthor']",docauthor)

            sql = "insert into pachong_table (id,doctitle,docpubtime,dockeywords,docpuburl,docabstract,docreltime,subdoctitle,imgsrc,docauthor) " \
                  "values (%s%s%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s');" \
                  % (list[a], page, i, doctitle, docpubtime, dockeywords, docpuburl, docabstract, docreltime,subdoctitle,imgsrc,docauthor)
            # print(sql)
            cursor.execute(sql)
            conn.commit()
            i += 1
        # count_xunhuan+=1
        break



count = 0
url_1 = "https://esearch.citicbank.com/search/action/information.jsp"
list = [3676,3677,3678,3679,3680,3681,3682,3683,3688,4074,4195,4244]

for a in range(len(list)):
    for page_1 in range(1, 305):
        url_now = url_1 + "?docchnl=" + str(list[a]) + "&currPage=" + str(page_1)
        page = '%04d' % page_1
        print("a---page  ",a+1,page)
        pachong(url_now,page)

        count+=1
print("count======   ",count)






