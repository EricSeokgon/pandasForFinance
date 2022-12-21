from pandas import DataFrame, Series

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

s = Series(data=[1600, 1600, 1600], index=df.index)
df["목표가"] = s
print(df)
