from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
cond = df["현재가"] >= 1400
print(df.loc[cond])
print(df.loc[cond]["현재가"])
print(df.loc[cond, "현재가"])

cond = (df["현재가"] >= 1400) & (df["현재가"] < 1700)
print(df.loc[cond])
