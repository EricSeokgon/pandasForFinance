from pandas import Series

data = [42500, 42550, 41800, 42550, 42650]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
s = Series(data=data, index=index)
cond = s > 4200
print(cond)

print(s[cond])
