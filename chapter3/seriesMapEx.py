from pandas import Series

s = Series(["1,234", "5,678", "9,876"])


# print(int(s)) # TypeError: cannot convert the series to <class 'int'>

def remove_comma(x):
    print(x, 'in function')
    return x


s = Series(["1,234", "5,678", "9,876"])
result = s.map(remove_comma)
print(result)
