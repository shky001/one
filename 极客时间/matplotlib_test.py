import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
import pandas as pd
import seaborn as sns
import warnings

# 绘制简单的曲线
# plt.plot( [1,3,5],[4,8,6] )
plt.show()

# 绘制numpy曲线---计算的值
x = np.linspace(-np.pi,np.pi,100)           # 产生一条直线
# plt.plot(x,sin(x))
plt.show()

# # 绘制多条曲线
# x = np.linspace(-np.pi*2,np.pi*2,100)               # x轴为 -2pi到2pi
# # 创建一个图表，精度为50
# plt.figure(1,dpi=50)                         # dpi表示绘画图形的详细程度，dpi越高，越清晰
# # for循环，绘制四条图线
# for i in range(1,5):
#     plt.plot(x,sin(x/i))
# plt.show()



# # 绘制其他图形---直方图（hist)
# plt.figure(1,dpi=50)
# data = [1,1,2,2,3,3,4,5,6]
# plt.hist(data)                      # 传入数据，直方图统计数据
# plt.show()

# # 散点图
# # x = [0,1,2,3,4,5,6,7,8,9]
# x = np.arange(10)
# y = x
# fig = plt.figure()          # 创建对应图表
# plt.scatter(x,y,c='r',marker='o')
# plt.show()



# # pandas结合matplotlib
# # 读取文件，会基于逗号分隔字段
# iris = pd.read_csv("./iris_training.csv")
# print(iris.head())                  # 读取前五行并输出
# # 基于前两列绘制散点图,x轴为'120'列，y轴为'4'列
# iris.plot(kind='scatter',x='120',y='4')
# plt.show()


# # 新的库---seaborn,封装Matplotlib
# iris = pd.read_csv("./iris_training.csv")
# print(iris.head())
# # 设置样式
# sns.set(style = 'white', color_codes = True)
# # 设置绘制格式为散点图
# sns.jointplot( x = '120',y = '4', data=iris,size=5 )
# # displot 绘制曲线
# sns.distplot(iris['120'])
# plt.show()


# 解决警告与单一颜色问题
warnings.filterwarnings("ignore")               # 忽略
iris = pd.read_csv("./iris_training.csv")
print(iris.head())
# 设置样式
sns.set(style = 'white', color_codes = True)
sns.FacetGrid(iris,hue="virginica")\
    .map(plt.scatter,'120','4')\
    .add_legend()
# sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "setosa", "versicolor").add_legend()
plt.show()
