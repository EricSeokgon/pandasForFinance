from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
df.rename(columns={'종목명': 'code'}, inplace=True)
print(df)

# print(df.columns)
# print(df.index)

# df.columns = ['name', 'close', 'fluctuation']  # 컬럼 이름 변경
# df.index.name = 'code'
# print(df)
