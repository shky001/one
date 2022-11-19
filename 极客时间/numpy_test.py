import numpy as np

arr1 = np.array([2,3,4])
print(arr1)
print(arr1.dtype)
arr2 = np.array([1.1,2.2,3.3])
print(arr2.dtype)

print(arr1 + arr2)
print(arr1*10)

# 定义二维数组
data = [[1,2,3],[4,5,6]]
arr3 = np.array(data)
print(arr3)

# 全为0、全为1
print(np.zeros(6))
print(np.zeros((2,3)))
print(np.ones((3,4)))
# 矩阵全置为空值
print(np.empty((2,3,4)))

# 索引和切片
arr4 = np.arange(10)
print(arr4[5])
print(arr4[5:8])
arr4[5:8] = 10

# 副本  重新赋值，原有数组不变
arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
