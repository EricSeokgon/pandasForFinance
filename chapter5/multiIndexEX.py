from pandas import DataFrame
import pandas as pd

data = [
    ['영업이익', '컨센서스', 1000, 1200],
    ['영업이익', '잠정치', 900, 1400],
    ['당기순이익', '컨센서스', 800, 900],
    ['당기순이익', '잠정치', 700, 800],
]

df = DataFrame(data=data)
df = df.set_index([0, 1])
print(df.iloc[0,0])

a = [1,2,3,4,5]
print(a[0:5:2])
print(a[slice(0,5,2)])

a = [1,2,3,4,5]
b = [3,4,5,6,7]

s=slice(0,5,2)
print(a[s])
print(b[s])

a = [1,2,3,4,5]
print(a[:])
print(a[slice(None)])
print(a[::])
print(a[slice(None,None)])
