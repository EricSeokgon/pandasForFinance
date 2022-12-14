from pandas import Series

data = [1000, 2000, 3000]
s = Series(data=data)

# iloc 연산을 사용해서 행번호로 인덱싱 양수/음수 모두 사용가능
print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])

data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

print(s.iloc[0])
print(s.loc['메로나'])

# s1은 rangeIndex타입 인덱스가 자동으로 부여된 상태이며 인덱스는 0을 통해 10이 출력
# s2는 인덱스를 1,2,3으로 각각 맵핑되어 인덱스0은 없어 에러
s1 = Series([10, 20, 30])
s2 = Series([10, 20, 30], index=[1, 2, 3])
print(s1[0])
# print(s2[0])

s3 = Series([10, 20, 30], index=['a', 'b', 'c'])
print(s3[0])
print(s3.index[0])
print(s3.index[-1])