import numpy as np

# ndarray와의 연산은 브로드캐스팅이 적용되어 전체 데이터에 연산이 반복 적용됨
arr = np.array([10, 20, 30])
print(arr > 10)
