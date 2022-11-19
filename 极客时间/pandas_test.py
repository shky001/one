import pandas as pd
from pandas import Series,DataFrame
from numpy import nan as NA

# # pandas的一维数组
# obj = Series([5,6,7,8])
# print(obj)
# # 单独取出obj的索引和值
# print(obj.index)                    # RangeIndex(start=0, stop=4, step=1)
# print(obj.values)                   # [5 6 7 8]

# # Series的基本操作
# obj2 = Series([2,4,6,8],index=['a','b','c','d'])
# print(obj2)
# obj2['a'] = 10             # 对索引进行赋值
# print(obj2)
# print('c' in obj2)                      # True

# # 数据为字典类型
# sdata = {'one':111,'two':222}
# obj3 = Series(sdata)
# print(obj3)
# obj3.index = ['ONE','TWO']                  # 修改索引
# print(obj3)



# DataFrame的基本操作
data = {'A':['aa','aaa'],'B':['bb','bbb']}
frame = DataFrame(data)
# print(frame)
# 按照指定顺序显示
frame2 = DataFrame(data,columns=['B','A'])
# print(frame2)
# 从二维表格中提取一维数据  []   .
# print(frame['A'])
# print(frame.A)

# 增加一列
frame['CC-new'] = 12                # 人工赋值
# print(frame)
frame['DD-new'] = frame.A == 'aa'               # 计算赋值
print(frame)

# 字典的嵌套
dict_my = {'bj':{3:4,5:6},'sh':{3:7,5:8}}
frame3 = DataFrame(dict_my)
# print(frame3)
# print(frame3.T)                      # 行列的互换（转置）

# 重新索引---修改原有
obj01 = Series([1,2,3],index=['a','b','c'])
# print(obj01)
obj02 = obj01.reindex(['A','B','C','D'],fill_value=0)
# print(obj02)

# 填充相邻元素的值
obj_new = Series(['x','y','z'],index=[0,2,4])           # 指定索引
# print(obj_new)
# print(obj_new.reindex(range(6),method='ffill'))         # 填充上一个值
# print(obj_new.reindex(range(6),method='bfill'))         # 填充上一个值

# 将缺失的值删除
data_d = Series([1,NA,2])
# print(data_d)
# print(data_d.dropna())              # 删除
#删除整行为NA值
data2 = DataFrame([[1,2,3],[4,NA,NA],[NA,NA,NA]])
# print(data2)
# print(data2.dropna(how='all'))
# 删除整列为NA值
data2[4] = NA
print(data2)
# print(data2.dropna(axis=1,how='all'))

# 填充缺失值为0
data2.fillna(0,inplace=True)
print(data2)
