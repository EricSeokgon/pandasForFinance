from pandas import Series

# 시리즈 슬라이싱
data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)
print(s.iloc[0:2])
