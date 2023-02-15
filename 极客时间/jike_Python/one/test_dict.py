# 请你设计一个字典数据类型用于存储通讯录，通讯录中包含：必须填写的姓名、可以为空的备注名、
# 1 个邮箱，至少 2 个手机号码，并尝试增加和删除联系人。

import pprint
from tinydb import TinyDB

with open("./24-demo.csv", encoding='utf-8') as f:
    file_data = f.readlines()
    pprint.pprint(file_data)

# 指定存放通讯录的文件
db = TinyDB('./db.json')
# 格式转换csv文件，存入通讯录文件
friend1 = {'name':file_data[0].split(",")[0],'source':file_data[0].split(",")[1],'tel':file_data[0].split(",")[2].strip()}
friend2 = {'name':file_data[1].split(",")[0],'source':file_data[1].split(",")[1],'tel':file_data[1].split(",")[2].strip()}
friend3 = {'name':file_data[2].split(",")[0],'source':file_data[2].split(",")[1],'tel':file_data[2].split(",")[2].strip()}

# 将通讯录好友信息写入数据库
db.insert_multiple([
    friend1,
    friend2,
    friend3
])

# 查看通讯录中全部好友
db.all()
# 根据姓名查电话
from tinydb import Query
friend = Query()
friend_info = db.search(friend.name == "张三")
print(friend_info)
print(friend_info[0]['name'] + "电话为：" + friend_info[0]['tel'])


# # 统计单词次数
# import pprint
# with open("./24-demo.txt") as f:
#     file_data = f.readlines()
#     # pprint.pprint(file_data)
# print(len(file_data))
# # 空行行数
# print(file_data.count("\n"))
# # 非空行行数
# print(len(file_data) - file_data.count("\n"))
# print(len(set(file_data)) - 1)
# # 单词I次数
# print(str(file_data).split(" ").count("I"))
# # 单词you 、 You次数
# print(int(str(file_data).split(" ").count("you")) + int(str(file_data).split(" ").count("You")))



#
# # 已知有两个列表，分别为:
# # [ 'name1', 'name2', 'name3' ]
# # [ '1111', '2222', '3333']
# # 现需要将这两个列表组成一个如下字典，请编写程序实现：
# # { 'name1':'1111', 'name2':'2222', 'name3':'3333' }
#
# list1 = [ 'name1', 'name2', 'name3' ]
# list2 = [ '1111', '2222', '3333']
# dict = {list1[0]:list2[0],list1[1]:list2[1],list1[2]:list2[2]}
# # print(dict)                     # {'name1': '1111', 'name2': '2222', 'name3': '3333'}
#
# # print(dict.items(),"\n",dict.keys(),"\n",dict.values())
# # print(dict.get('name1'))
# # for key,value in dict.items():
# #     print(key)
# #     print(value)
# # print(dict.pop('name1'))                # 1111
# # print(dict.popitem())                   # ('name3', '3333')
# dict1 = dict.setdefault('name1')
# # print(dict1)                    # 1111
# dict2 = dict.setdefault('name_new',12345)
# # print(dict2)                        # 12345
# print(dict)
# # dict_new = {'n1': '11', 'n2': '22', 'n3': '33', 'n4': 44}
# # dict |= dict_new
