from pandas import Series

data = [42500, 42550, 41800, 42550, 42650]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
s = Series(data=data, index=index)
cond = s > 4200
print(cond)
print(s[cond])

close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)
cond = close > open
print(cond)
print(close[cond])
print(close[close > open])  # 변수를 사용하지 않고 한줄로 짧게 표현

print(close.index[close > open])
print(close[close > open].index)

close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)
diff = close - open
print(diff[close > open])
