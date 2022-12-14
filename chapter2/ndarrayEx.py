import numpy as np

data1 = [1, 2, 3, 4]
arr1 = np.array(data1)
print(arr1)
print(type(arr1))

data2 = [
    [1, 2],
    [3, 4]
]

arr2 = np.array(data2)
print(arr2)
print(type(arr2))
print(type(arr2[0]))
print(arr2.shape)
print(arr2.ndim)
print(arr2.dtype)
print(arr1.shape)

data = [
    [1],
    [2],
    [3],
    [4]
]

c = np.array(data)
print(c.shape)

print(np.zeros(3))
print(np.ones(3))

#zeros,ones 함수의 인자로 튜플을 전달하면 0, 1로 구성된 다차원 배열을 생성할 수있다.
size = (3, 4)
print(np.zeros(size))
print(np.zeros((3, 4)))
