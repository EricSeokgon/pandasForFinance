from pandas import DataFrame

data = {
    '종목코드': ['037730', '06360', '005760'],
    '종목명': ['3R', '3SOFT', 'ACTS'],
    '현재가': [1510, 1790, 1185]
}

df = DataFrame(data)  # DataFrame 클래스의 객체 생성 (생성자 호출)
print(df)
