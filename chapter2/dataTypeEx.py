import numpy as np

arr = np.array([1, 2, 3], dtype=np.uint8)
print(arr.dtype)
print(arr.dtype.kind)
print(arr.dtype.alignment)

# astype 메서드를 사용해서 기존의 ndarray를 다른 타입으로 변경할 수 있다.
arr = arr.astype('int8')
print(arr.dtype)

# b의 데이터 타입 int8은 -128~127까지만 표현
a = np.array([0, 255], dtype=np.uint8)
b = a.astype('int8')
print(a)
print(b)


