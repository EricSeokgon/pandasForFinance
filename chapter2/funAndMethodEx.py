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
np.random.randint(46, size=(2, 5))

# linspace 첫번째는 시작 값, 두번째는 종료값, 세번째는 분할 지점의 수
x = np.linspace(0, 10, 3)
print(x)

y = x ** 2

# 넘파이의 stack함수는 여러 개의 ndarray를 하나로 합칠 때 사용
# vstack 수직, hstack은 수평
a = np.arange(4)
b = np.arange(4, 8)
c = np.vstack([a, b])
print(c)
