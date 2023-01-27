from pandas import DataFrame

data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
    ["850", "900", "1,185"]
]
columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
print(df)


def remove_comma(x):
    return int(x.replace(',', ''))


# df['03/02'] = df['03/02'].map(remove_comma)
# df['03/03'] = df['03/03'].map(remove_comma)
# df['03/04'] = df['03/04'].map(remove_comma)
df = df.applymap(remove_comma)
print(df)
print(df.dtypes)
