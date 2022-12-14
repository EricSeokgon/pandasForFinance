from pandas import Series
import numpy as np

# 시리즈 생성
# data = [10, 20, 30]
data = np.arange(5)
s = Series(data)
print(s)
