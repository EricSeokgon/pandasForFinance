from pandas import Series
# 시리즈 연산
철수 = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
영희 = Series([10, 20, 30], index=['SKT', 'KT', 'NAVER'])
가족 = 철수 + 영희
print(가족)
