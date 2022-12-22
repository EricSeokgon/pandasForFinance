from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

df_new = df.drop("현재가", axis=1)
print(df)
print(df_new)

df_new = df.drop("037730", axis=0)
print(df)
print(df_new)

df.drop(["037730", "005760"], axis=0, inplace=True)
print(df)
