# 层次化索引
import numpy as np
from pandas import Series,DataFrame

# 定义一组数据（两列）
data = Series(np.random.randint(1,10),[ ['a','a','a','b','b','b','c','c','d','d'],
                                    [1,2,3,1,2,3,1,2,2,3] ])
print(data)
print(data['a'])            # 根据层次提取索引
print(data['a':'b'])        # 输出多个索引

# 一维数据 --> 二维数据
print(data.unstack())
print(data.unstack().stack())
