from pandas import DataFrame

data = {
    '종목코드': ['037730', '06360', '005760'],
    '종목명': ['3R', '3SOFT', 'ACTS'],
    '현재가': [1510, 1790, 1185]
}

df = DataFrame(data)  # DataFrame 클래스의 객체 생성 (생성자 호출)
print(df)

data = [
    ["037730", "3R", 1510],
    ["06360", "3SOFT", 1790],
    ["005760", "ACTS", 1185]
]
columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
print(df)

data = [
    {"종목코드": "037730", "종목명": "3R", "현재가": 1510},
    {"종목코드": "06360", "종목명": "3SOFT", "현재가": 1790},
    {"종목코드": "005760", "종목명": "ACTS", "현재가": 1185}
]
df = DataFrame(data=data)
print(df)
