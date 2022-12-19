from pandas import Series


def remove_comma(x):
    return int(x.replace(",", ""))


s = Series(["1,234", "5,678", "9,876"])
result = s.map(remove_comma)
print(result)


def is_greater_than_5000(x):
    if x > 5000:
        return "크다"
    else:
        return "작다"


s = Series([1234, 5678, 9876])
s = s.map(is_greater_than_5000)
print(s)
