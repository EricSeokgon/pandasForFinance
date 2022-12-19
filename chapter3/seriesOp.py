from pandas import Series

# 시리즈 연산
철수 = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
영희 = Series([10, 20, 30], index=['SKT', 'KT', 'NAVER'])
가족 = 철수 + 영희
print(가족)
print(철수 * 10)

high = Series([42800, 42700, 42050, 42950, 43000])
low = Series([42150, 42150, 41300, 42150, 42350])

diff = high - low
print(diff)
print(diff.max())

date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
high = Series([42800, 42700, 42050, 42950, 43000], index=date)
low = Series([42150, 42150, 41300, 42150, 42350], index=date)
diff = high - low
print(diff)

max_idx = 0
max_val = 0
for i in range(len(diff)):
    if diff[i] > max_val:
        max_val = diff[i]
        max_idx = i
print(max_idx)
print(diff.index[max_idx])

print(diff.idxmax())
print(diff.idxmin())
