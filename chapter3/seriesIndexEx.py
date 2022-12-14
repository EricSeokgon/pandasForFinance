from pandas import Series

# 시리즈 인덱스
data = [1000, 2000, 3000]
s = Series(data)
print(s.index)
print(s.index.to_list())
