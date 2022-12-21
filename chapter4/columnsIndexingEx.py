from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print(df['현재가']) #데이터 프레임의 인덱싱
print(df.현재가)
리스트 = ["현재가","등락률"]
print(df[리스트])
print(df[["현재가","등락률"]])
print(df[['현재가']]) # 데이터프레임의 한개 컬럼 슬라이싱
print(df.loc["037730"])