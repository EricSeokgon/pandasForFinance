from pandas import Series

price = [42500, 42550, 41800, 42550, 42650]
date = ["2019-05-31", "2019-05-30", "2019-05-29", "2019-05-28", "2019-05-27"]
s = Series(price, date)
print(s)

# 딕셔너리를 사용해서 시리즈를 한번에 작성

data = {
    "2019-05-31": 42500,
    "2019-05-30": 42550,
    "2019-05-29": 41800,
    "2019-05-28": 42550,
    "2019-05-27": 42650
}

s = Series(data)

# 딕셔너리 객체에서 keys와 values 메서드를 사용하는 것과 유사하게 시리즈 객체는 index와 values라는 속성을 통해 인덱스와 값을 각각 분리해서 얻어올수 있다.
print(s.index)
print(s.index.dtype)
print(s.values)