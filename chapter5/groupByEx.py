from pandas import DataFrame
import pandas as pd
import numpy as np

data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = DataFrame(data=data, columns=columns)
df1 = df[df['테마'] == "2차전지(생산)"]
df2 = df[df['테마'] == "해운"]
df3 = df[df['테마'] == "시스템반도체"]

mean1 = df1['PER'].mean()
mean2 = df2['PER'].mean()
mean3 = df3['PER'].mean()

data = [mean1, mean2, mean3]
index = ["2차전지(생산)", "해운", "시스템반도체"]
s = pd.Series(data=data, index=index)

df.groupby("테마")["PER"].mean()
gb = df.groupby("테마")
temp = gb.get_group("2차전지(생산)")
print(temp)

temp = df[["테마", "PER", "PBR"]].groupby("테마").get_group("2차전지(생산)")
print(temp)

temp = df.groupby("테마")[["PBR", "PBR"]].get_group("2차전지(생산)")
print(temp)

df.groupby("테마")[["PER", "PBR"]].mean()
df.groupby("테마").mean()

# df.groupby("테마").agg({"PER": max, "PBR": min})
df.groupby("테마").agg({"PER": [min, max], "PBR": [np.std, np.var]})

# 첫 번쨰 데이터프레임
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 292163]
}

index = ['2019-06-21', '2019-06-20']
df1 = DataFrame(data=data, index=index)

# 두 번째 데이터프레임
data = {
    '시가': [112500, 110000],
    '고가': [115000, 112000],
    '저가': [111500, 109000]
}

index = ['2019-06-21', '2019-06-20']
df2 = DataFrame(data=data, index=index)

df = pd.concat([df1, df2], axis=1, join='inner')
print(df)

# 정렬순서 = ['시가', '고가', '저가', '종가', '거래량']
# df = df[정렬순서]
# print(df)
