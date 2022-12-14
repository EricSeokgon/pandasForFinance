from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print(df['현재가'])  # 데이터 프레임의 인덱싱
print(df.현재가)
리스트 = ["현재가", "등락률"]
print(df[리스트])
print(df[["현재가", "등락률"]])
print(df[['현재가']])  # 데이터프레임의 한개 컬럼 슬라이싱
print(df.loc["037730"])
print(df.iloc[0])
print(df.iloc[-1])

# 행 번호로 행 선태 후 시리즈 인덱싱
print(df.iloc[0].iloc[1])  # 시리즈 행 번호
print(df.iloc[0].loc["현재가"])  # 시리즈 인덱스
print(df.iloc[0]["현재가"])  # 시리즈 인덱스

# 인덱스로 행 선택 후 시리즈 인덱싱
print(df.loc["037730"].iloc[1])  # 시리즈 행 번호
print(df.loc["037730"].loc["현재가"])  # 시리즈 인덱스
print(df.loc["037730"]["현재가"])  # 시리즈 인덱스

print(df.loc["037730", "현재가"])
print(df.iloc[0, 1])

print(df["현재가"].iloc[0])
print(df["현재가"].loc["037730"])
print(df["현재가"]["037730"])

# 특정 범위 가져오기
print(df.loc[["037730", "036360"]])
print(df.iloc[[0, 1]])

df = df.loc[["037730", "036360"]]
df = df[["종목명", "현재가"]]
print(df)

print(df.loc[["037730", "036360"], ["종목명", "현재가"]])
print(df.iloc[0, 1], [0, 1])
