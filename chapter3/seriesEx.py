from pandas import Series
import numpy as np

# 시리즈 생성
# data = [10, 20, 30]
data = np.arange(5)
s = Series(data)
print(s)

# 두개의 문자열을 저장하는 시리즈 객체 생성

data = ["시가", "고가"]
s = Series(data)
print(s)
