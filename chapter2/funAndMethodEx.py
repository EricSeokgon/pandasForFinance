import numpy as np

# 넘파이는 수치연산과 관련된 다양한 함수와 메서드를 제공
arr = np.arange(8).reshape(4, 2)
print(arr.sum())

# sum메서드에 축정보를 지정할 수있다.
print(arr.sum(axis=0))
