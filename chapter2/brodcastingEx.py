import numpy as np

# 같은 인덱스를 갖는 데이터 간의 연산이 적용
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(a + b)
print(a * b)
print(a % b)

# 스칼라 연산은 전체 데이터에 확장 적용
print(a + 3)
