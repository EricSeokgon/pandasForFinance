from pandas import Series

# 시리즈 슬라이싱
data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

# iloc[시작 행번호:끝 행번호], loc[시작 인덱스: 끝 인덱스]
print(s.iloc[0:2])
print(s.loc['메로나':'구구콘'])
