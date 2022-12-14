import numpy as np

arr = np.array([1, 2, 3], dtype=np.uint8)
print(arr.dtype)
print(arr.dtype.kind)
print(arr.dtype.alignment)

# astype 메서드를 사용해서 기존의 ndarray를 다른 타입으로 변경할 수 있다.
arr = arr.astype('int8')
print(arr.dtype)
