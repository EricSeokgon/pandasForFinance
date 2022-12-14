from pandas import Series

data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

s.loc['메로나'] = 500  # 값 수정
print(s)
s.iloc[0] = 500  # iloc 연산 사용
s['메로나'] = 500  # []기호 사용

s.loc['비비빅'] = 500  # 값 추가
print(s)
