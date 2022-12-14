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

a16 = np.array([1.333333], dtype=np.float16)
a32 = np.array([1.333333], dtype=np.float32)
print(a16)
print(a32)

a16 = np.array([1.0], dtype=np.float16)
a32 = np.array([1.0], dtype=np.float32)
print(a16 / 3)
print(a32 / 3)

# nan은 Not a Number의 약자로 숫자가 아닌 값 혹은 저으이도지 않는 숫자
# inf 혹은 -inf는 무한대의 숫자를 뜻함
print(np.nan, type(np.nan))
print(np.inf, type(np.inf))
print(-np.inf, type(-np.inf))

arr = np.array([-1, 2, -3])
# print(arr / 0)

# 결측치에 숫자를 더하면 넘파이는 결측값을 반환
arr = np.array([-1, 2, -3])
print(arr + np.nan)
print(arr + np.inf)
