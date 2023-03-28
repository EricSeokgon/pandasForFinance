from pandas import DataFrame
import pandas as pd

data = [
    [1000, 900, 800, 700],
    [1200, 1400, 900, 800],
]

level_0 = ['영업이익', '당기순이익']
level_1 = ['컨센서스', '잠정치']
columns = pd.MultiIndex.from_product([level_0, level_1])

df = DataFrame(data=data, index=["2020/06", "2020/09"], columns=columns)
print(df.stack())
