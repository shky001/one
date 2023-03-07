
# 请使用并发任务模型同时访问 5 个网站，并将网页的数据存储到不同的文件中。

from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

URLS = [
  'https://time.geekbang.org',
  'https://www.taobao.com/',
  'https://www.jd.com',
  'https://leetcode.cn',
  'https://www.zhihu.com'
]

def load_url(url, timeout):
  with urllib.request.urlopen(url, timeout=timeout) as conn:
    return conn.read()

with ThreadPoolExecutor(max_workers=5) as executor:
  future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
  for future in as_completed(future_to_url):
    url = future_to_url[future]

    try:
      data = future.result().decode('utf-8')
    except Exception as exc:
      print('%r generated an exception: %s' % (url, exc))
    else:
      # url 可以继续处理
      with open(r"url.txt", 'w+', encoding='utf-8') as f:
        f.write(data)
      print('%r page is saved' % (url))