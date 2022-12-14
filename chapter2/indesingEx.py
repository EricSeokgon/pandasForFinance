import numpy as np

# arr[0]은 arr에 바인딩된 넘파이 객체의 0번째 데이터를 반환
arr = np.arange(4)
print(arr[0])

# 2차원 ndarray의 경우 인덱싱은 기본적으로 행에 우선 적용
arr = np.arange(4).reshape(2, 2)
print(arr[0])

a = np.arange(10000).reshape(100, 100)

arr = np.arange(4)
print(arr[:2])

# 리스트의 기능에 추가해서 ndarray는 불연속적인 데이터를 슬라이싱할 수 있다.
target = [0, 2]
print(arr[target])

# 4행 5열로 구성된 ndarray에서 두개의 행을 슬라이싱
arr = np.arange(20).reshape(4, 5)
print(arr[:2])
