# 结合正则表达式爬取图片链接
import re
import requests

contents = requests.get('http://www.cnu.cc/users/1059128').text
# print(contents)

# re.S	使 . 匹配包括换行在内的所有字符
pattern = re.compile(r'<a href="(.*?)".*?"title">(.*?)</div>',re.S)
results = re.findall(pattern,contents)
# print(results)
for i in results:
    # print(i)
    url,name = i
    print(url,"   ——————   ",re.sub('\s','',name))

"""
<div class="col-xs-6 col-sm-4 col-md-3 work-thumbnail">
                <a href="http://www.cnu.cc/works/586225" class="thumbnail" target="_blank">
                    <div class="title">
                        太阳太远了，否则我要埋在那里
                    </div>
                    <div class="author">
                        2022-07-25
                    </div>
                                                                <div class="count">
                            0
                        </div>
                                        <img src="http://imgoss.cnu.cc/2207/25/aexxgd10i91oxc0mxdy1658708192298.jpg?width=280&x-oss-process=style/cover280" alt="...">
                </a>
            </div>"""

