from pandas import DataFrame

data = [
    {"cd": "A060310", "nm": "3S", "open": 2920, "close": 2800},
    {"cd": "A095570", "nm": "AJ네트웍스", "open": 1920, "close": 1900},
    {"cd": "A006840", "nm": "AK홀딩스", "open": 2020, "close": 2010},
    {"cd": "A054620", "nm": "APS홀딩스", "open": 3120, "close": 3200}
]
df = DataFrame(data=data)
df = df.set_index('cd')
print(df)

cond = df['open'] >= 2000
print(df[cond])
