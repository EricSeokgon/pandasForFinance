from pandas import Series


def remove_comma(x):
    return int(x.replace(",", ""))

s = Series(["1,234", "5,678", "9,876"])
result = s.map(remove_comma)
print(result)
