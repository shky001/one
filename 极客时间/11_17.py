# import queue
# q = queue.Queue()
# q.put(1)
# print(q.get())

# # 40   经典的生产者和消费者问题
# import queue
# from threading import Thread,current_thread
# import random
# import time
# from queue import Queue
# q = queue.Queue(5)              # 定义队列长度为5
# class ProducerThread(Thread):
#     def run(self):
#         name = current_thread().getName()
#         nums = range(100)
#         global q
#         while True:
#             num = random.choice(nums)
#             q.put(num)
#             print("生产者%s生产了数据%s" %(name,num))
#             t = random.randint(1,3)
#             time.sleep(t)
#             print("生产者%s睡眠了%s秒" %(name,t))
# class ConsumerThread(Thread):
#     def run(self):
#         name = current_thread().getName()
#         global q
#         while True:
#             num = q.get()
#             # q.taskdone()
#             print("消费者%s消费了数据%s" % (name, num))
#             t = random.randint(1, 3)
#             time.sleep(t)
#             print("消费者%s睡眠了%s秒" % (name, t))
# p1 = ProducerThread(name='p1')
# p1.start()
# c1 = ConsumerThread(name='c1')
# c1.start()
# c2 = ConsumerThread(name='c2')
# c2.start()



# # 42   正则表达式库
# import re
# p = re.compile('a')
# print(p.match('a'))             # <re.Match object; span=(0, 1), match='a'>
# print(p.match('bcdefg'))        # None



# # 43   正则表达式的元字符
# #     .     ^   $   *   +   ?   {m} {m,n}       []  \   \d  \D  \s      ()
# import re
# p = re.compile('...')
# print(p.match('abcdefgsunshine'))           # .   <re.Match object; span=(0, 3), match='abc'>
# p = re.compile('jpg$')
# print(p.match('jpg'))
# # * 零次或多次
# p = re.compile('ca*t')
# print(p.match('ct'))                        # *   <re.Match object; span=(0, 2), match='ct'>
# # + 一次或多次，至少需出现一次
# p = re.compile('ca+t')
# print(p.match('ct'))                    # None
# # ?   零次或一次
# p = re.compile('ca?t')
# print(p.match('caaat'))                 # None
# p = re.compile('ca{4}t')
# print(p.match('caaaat'))                  # <re.Match object; span=(0, 6), match='caaaat'>
# p = re.compile('c[bcd]t')
# print(p.match('cbt'))
# p = re.compile('ca.*?t')
# print(p.match('caaaaaaaat'))



# # 44   正则表达式分组功能实例
# import re
# p = re.compile('.{2}')                     # .与{}结合
# print(p.match('cat').group())              # ca
# print("sunshine\nsun")
# print(r"sunshine\nsun")                    # r 不转义
# 用()方式对年月日进行分组,group()默认取出所有字符，groups()全部取出
# import re
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2022-11-17').group(1))                # 2022
# year,month,date = p.match('2001-04-10').groups()
# print(year,month,date)                               # 2001 04 10



# # 45   正则表达式库函数match与search的区别
# import re
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('123-456-789').group())           # 匹配需与正则一一对应
# # match()包含则匹配
# print(p.search('abc12-34-56def').group())       # 12-34-56



# # 46   正则表达式库函数sub()的实例
# import re
# p1 = re.sub('c','a','qwer0c0asdf')
# print(p1)                                                   # qwer0a0asdf
# # 电话号码：去尾部  +  去-
# phone = '123-453-678   #this is my phonenumber!!!'
# p2 = re.sub('#.*$','',phone)
# print(p2)                                                   # 123-453-678
# p3 = re.sub(r'\D','',p2)
# print(p3)                                                   # 123453678

# # findall()可匹配多次,函数可传两个参数。
# import re
# p = re.compile(r'\d+')
# print(p.findall('one1two2three3four4'))
# p2 = re.compile(r'\d+')
# print(re.findall(p2, "one123"))



# # 47   日期与时间函数库
# import time
# print(time.time())              # 1. 直接输出为： 1668675812.7596323
# print(time.localtime())         # 2. 封装---转换为年月日
# # time.struct_time(tm_year=2022, tm_mon=11, tm_mday=17, tm_hour=17, tm_min=7, tm_sec=28, tm_wday=3, tm_yday=321, tm_isdst=0)
# print(time.strftime('%Y-%m-%d   %H:%M:%S'))                 # 3. 格式化输出，自定义格式： 2022-11-17   17:07:28

# import datetime
# # 1. 当前时间
# print(datetime.datetime.now())                          # 2022-11-17 17:12:43.725146
# # 2. 当前时间10分钟后时间
# newtime = datetime.timedelta(minutes=10)
# result_time = datetime.datetime.now() + newtime
# print(result_time)                                      # 2022-11-17 17:22:43.725146
# # 3. 指定日期的后十天
# oneday = datetime.datetime(2001,9,10)
# newtime_2 = datetime.timedelta(days=10)
# print(oneday + newtime_2)                               # 2001-09-20 00:00:00



# # 48   数学相关库
# import random
# print(random.randint(1,10))
# print(random.choice(['aaa','bbb','ccc']))



# # 50   文件与目录操作库
# # 1. os.Path库
# import os
# # 根据相对路径获取绝对路径
# print(os.path.abspath('.'))                 # C:\Users\31872\Desktop\001\jikeshijian
# print(os.path.abspath('..'))                # C:\Users\31872\Desktop\001
# # ① 判断文件是否存在
# print(os.path.exists('\\Users'))                    # True
# # ② 判断是否为文件
# print(os.path.isfile('\\jikeshijian'))              # False
# # ③ 判断是否为目录
# print(os.path.isdir('\\Users'))                     # True
# # ④ 路径的拼接
# os.path.join('','b/c')

# 2. pathlib库
from pathlib import Path
# 根据相对路径获取绝对路径
p = Path('.')                   # 封装为p
print(p.resolve())              # C:\Users\31872\Desktop\001\jikeshijian
# pathlib库可新建目录
q = Path('/aaaaaa')          # 定义完整路径
Path.mkdir(q,parents=True)
print("________________________________________")
