from pandas import DataFrame
import pandas as pd

data = [
    [1000, 1100, 900, 1200, 1300],
    [800, 2000, 1700, 1500, 1800],
]

index = ['자본금', '부채']
columns = ["2020/03", "2020/06", "2020/09", "2021/03", "2021/06"]

df = DataFrame(data=data, columns=columns)
df_stacked = df.stack().reset_index()

temp = df_stacked['level_1'].str.split('/')
print(temp)
