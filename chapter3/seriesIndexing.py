from pandas import Series

data = [1000, 2000, 3000]
s = Series(data=data)

# iloc 연산을 사용해서 행번호로 인덱싱 양수/음수 모두 사용가능
print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])
