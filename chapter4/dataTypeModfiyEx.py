from pandas import DataFrame

data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
    ["850", "900", "1,185"]
]
columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
print(df)


