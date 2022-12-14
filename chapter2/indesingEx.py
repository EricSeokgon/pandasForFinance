import numpy as np

# arr[0]은 arr에 바인딩된 넘파이 객체의 0번째 데이터를 반환
arr = np.arange(4)
print(arr[0])

# 2차원 ndarray의 경우 인덱싱은 기본적으로 행에 우선 적용
arr = np.arange(4).reshape(2,2)
print(arr[0])