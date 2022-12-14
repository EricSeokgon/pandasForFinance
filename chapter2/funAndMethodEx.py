import numpy as np

# 넘파이는 수치연산과 관련된 다양한 함수와 메서드를 제공
arr = np.arange(8).reshape(4, 2)
print(arr.sum())

# sum메서드에 축정보를 지정할 수있다.
print(arr.sum(axis=0))
print(arr.sum(axis=1))

# 넘파이를 사용해서 임의의 숫자를 만들 수도 있다.
np.random.randint(3)

# size 옵션을 사용하면 생성되는 숫자의 개수를 지정할 수있다.
np.random.randint(46, size=5)
np.random.randint(46, size=(2,5))
