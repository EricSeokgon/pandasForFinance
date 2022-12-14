from pandas import Series

# 시리즈 인덱스
data = [1000, 2000, 3000]
s = Series(data)
print(s.index)
print(s.index.to_list())

data = [1000, 2000, 3000]
s = Series(data)
s.index = ["메로나", "구구콘", "하겐다즈"]
print(s)

# 시리즈를 생성할때 인덱스를 같이 지정
data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data, index)
print(s)

v = [1000, 2000, 3000]
k = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=v, index=k)

# reindex메서드를 사용하면 인자로 전달한 새로운 값으로 인덱스를 변경
# 기존에 있던 인덱스는 기존값을 기대로 사용하고, 새로운 인덱스는 NaN값으로 채움
data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)
s2 = s.reindex(["메로나", "비비빅", "하겐다즈"])
print(s2)
