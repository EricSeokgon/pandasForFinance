import numpy as np

# ndarray와의 연산은 브로드캐스팅이 적용되어 전체 데이터에 연산이 반복 적용됨
arr = np.array([10, 20, 30])
print(arr > 10)

# 인덱스의 리스트로 슬라이싱한 것과 유사하게 True와 False가 담긴 ndarray로 조건이 참인 데이터만 슬라이싱할 수있다.
arr = np.array([10, 20, 30])
cond = [False, True, True]
print(arr[cond])
