# # 18   列表推导式
# list_1 = []
# for i in range(1,11):
#     if (i % 2 == 0):
#         list_1.append(i*i)
# print(list_1)       # [4, 16, 36, 64, 100]
# print("------------")
# list_2 = [i*i for i in range(1,11) if(i%2==0)]
# print(list_2)       # [4, 16, 36, 64, 100]



# # 19   文件的内建函数
# file1 = open('name.txt','a',encoding='utf-8')
# file1.write('\n宋暖')
# file1.close()
# print("写入成功！")



# # 20   文件的常用操作
# file2 = open('name.txt',encoding='utf-8')
# print("当前文件的指针位置：",file2.tell())        #当前文件的指针位置： 0
# print(file2.read(2))               # 张三
# print("指针位于：",file2.tell())
# # file2.write('哇哈哈哈哈哈')



# # 21   异常的检测和处理
# try:
#     a,b = 2,0
#     c = a / b
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print("程序运行结束！")



# # 23-24   函数的可变长参数与变量作用域
# def howlong(first,*other):
#     print(1 + len(other))
# howlong(1,2,3,4,5)      # 5

# def func():
#     global var1
#     var1 = 'sunshine'
#     print(var1)
# func()
# print(var1)         # sunshine



# # 25   函数的迭代器与生成器
# list1 = [2,4,10]
# it = iter(list1)
# print(next(it))             # 2
# print(next(it))             # 4
# print(next(it))             # 10
# print(next(it))             # StopIteration

# # 循环输出浮点型数字
# def frange(start,end,step):
#     x = start
#     while x < end:
#         yield x
#         x += step
# for i in frange(10,12,0.5):
#     print(i)                        # 10,10.5,11.0,11.5



# # 26   lambda表达式
# fun2 = lambda x,y:x+y
# print(fun2(5,9))            # 14



# # 27   Python内建函数
# list_1 = [2,4,6,8,9]
# print(list(filter(lambda x:x>2,list_1)))        # [4, 6, 8, 9]
# a,b = [1,2,3],[6,7,8]
# print(list(map(lambda x,y:x+y,a,b)))            # [7, 9, 11]
# from functools import reduce
# print(reduce(lambda x,y:x+y,[2,3,4],1))           # 10
# for i in zip((1,2,3),(4,5,6)):
#     print(i)                                # (1, 4),(2, 5),(3, 6)



# 28-29   闭包的定义与使用
# def func():
#     a,b = 1,2
#     return a+b
# def sum(a):
#     def add(b):
#         return a+b
#     return add
# num1 = func()
# num2 = sum(6)
# print(num2(8),type(num1),type(num2))          # 14 <class 'int'> <class 'function'>

## 闭包实现计数器
# def counter(first=0):
#     cnt = [first]
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#     return add_one
# num5 = counter(5)
# print(num5())               # 6
# print(num5())               # 7

# # 闭包计算y=ax+b
# def a_line(a,b):
#     def func_y(x):
#         y = a*x + b
#         return y
#     return func_y
# line1 = a_line(3,6)
# print(line1(10))                # 36



# # 30-31   装饰器的定义与使用
# import time
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("运行时间为：  ",stop_time-start_time)
#     return wrapper
# @timmer
# def i_can_sleep():
#     time.sleep(3)
# i_can_sleep()                 # 运行时间为：   3.004023551940918

# 装饰器计算a+b，a-b
def newtips(argv):
    def tips(func):
        def nei(a,b):
            print("start!!!",argv,func.__name__)
            func(a,b)
            print("end!!!")
        return nei
    return tips
@newtips('add_module')
def add(a,b):
    print(a+b)
@newtips('sub_module')
def sub(a,b):
    print(a-b)
print(add(4,5))             # 9
print(sub(10,2))            # 8


