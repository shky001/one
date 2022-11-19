# # 33   模块的定义
# import mymod
# mymod.print_me()            # Hello,sunshine!



# # 35   类和实例
# # 面向过程编程
# user1 = {'name':'AAA','hp':100}
# def print_role(rolename):
#     print(rolename['name'],rolename['hp'])
# print_role(user1)                   # AAA 100
# 面向对象编程
# 定义一个类
# class Player():
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp
#     def print_role(self):
#         print(self.name,":",self.hp)
# user1 = Player('AAA',100)                   # 类的实例化
# user1.print_role()                          # AAA : 100



# # 36   如何增加类的属性和方法
# class Player():
#     def __init__(self,name,hp,occu):
#         self.__name = name          # 封装属性name
#         self.hp = hp
#         self.occu = occu
#     def print_role(self):
#         print(self.__name,":",self.hp)
#     def updateName(self,newname):
#         self.name = newname
# user1 = Player('AAA',100,'a1')
# user1.print_role()                       # AAA : 100
# user1.updateName('Aaaaa')
# user1.print_role()                       # Aaaaa : 100,,,,,,封装后： AAA : 100



# # 类的继承
# class Monster():
#     def __init__(self,hp = 200):
#         self.hp = hp
#     def run(self):
#         print("移动到某个位置！")
#     def who(self):
#         print("我是父类Monster!!!")
# class Animals(Monster):
#     def __init__(self,hp = 100):
#         super().__init__(hp)
# class Boss(Animals):
#     def __init__(self,hp = 1000):
#         super().__init__(hp)
#     def who(self):
#         print("子类Boss！！！")
# a1 = Monster(220)
# print(a1.hp)                # 220
# a1.run()                    # 移动到某个位置！
# # 类的继承
# a2 = Animals()
# a2.run()                    # 移动到某个位置！
# # 类的多态
# a3 = Boss()
# a3.who()                    # 子类Boss！！！
#
# # 判断子类
# print(type(a1))                                 # <class '__main__.Monster'>
# print(isinstance(a2,Monster))                   # True

# print(type(list))                               # <class 'type'>
# a = '123456'                                    # <class 'str'>
# print(type(a))
# print(isinstance(a,object))                        # True
# print(isinstance(123,object))                      # True



# # 38   类的使用——自定义with语句
# class Testwith():
#     def __enter__(self):
#         print("run")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_tb is None:
#             print("没有错误，正常结束！")
#         else:
#             print("error:  ",exc_tb)
# with Testwith():
#     print("running!!!")
#     raise NameError('testNameError')
# # run
# # running!!!
# # error:   <traceback object at 0x000001D6C7FB1480>



# # 多线程编程
# import threading
# import time
# from threading import current_thread
# def myThread(one,two):
#     print(current_thread().getName(),'start')
#     print(one,two)
#     time.sleep(1)
#     print(current_thread().getName(),'stop')
# for i in range(1,6,1):
#     #t1 = myThread(i, i+1)
#     t1 = threading.Thread(target=myThread,args=(i,i+1))
#     t1.start()                      # 运行程序
# print(current_thread().getName(),'end')


import threading
from threading import current_thread
class Mytyread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print("running!!!")
        print(current_thread().getName(),'stop')
t1 = Mytyread()
t1.start()
t1.join()
print(current_thread().getName(),'end')
# Thread-1 start
# running!!!
# Thread-1 stop
# MainThread end
