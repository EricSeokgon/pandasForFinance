import numpy as np

# 같은 인덱스를 갖는 데이터 간의 연산이 적용
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(a + b)
print(a * b)
print(a % b)

# 스칼라 연산은 전체 데이터에 확장 적용
print(a + 3)

high = [92700, 92400, 92100, 94300, 92300]
low = [90000, 91100, 91700, 92100, 90900]

arr_high = np.array(high)
arr_low = np.array(low)

arr_diff = arr_high - arr_low
print(arr_diff)

arr_high_x3 = arr_high * 3
arr_low_x2 = arr_low * 2
print(arr_high_x3 + arr_low_x2)

avg = (arr_high * 3) + (arr_low * 2)

data = [
    [92700, 92400, 92100, 94300, 92300],
    [90000, 91100, 91700, 92100, 90900]
]

# ndarray를 인덱싱해서 위와 유사하게 계산할수 있음
arr = np.array(data)
print(arr[0] * 3 + arr[1] * 2)

# 이차원 데이터의 브로드캐스팅을 용용해서 문제를 풀수 있음
weight = np.array([3, 2]).reshape(2, 1)
print((weight * arr).sum(axis=0))
