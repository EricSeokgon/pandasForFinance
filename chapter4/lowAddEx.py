from pandas import DataFrame, Series

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

s = Series(data=["LG전자", 60000, 3.84], index=df.columns)
df.loc["066570"] = s
print(df)

df.loc["066570"] = ['LG전자', 60000, 3.84]
print(df)

s = Series(data=["LG전자", 60000, 3.84], index=df.columns, name="066570")
new_df = df.append(s)
print(new_df)

