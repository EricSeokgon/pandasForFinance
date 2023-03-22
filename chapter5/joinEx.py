from pandas import DataFrame
import numpy as np
import pandas as pd

data = [
    ["2017", "삼성", 500],
    ["2017", "LG", 300],
    ["2017", "SK하이닉스", 200],
    ["2018", "삼성", 600],
    ["2018", "LG", 400],
    ["2018", "SK하이닉스", 300]

]

columns = ["연도", "회사", "시가총액"]
df = DataFrame(data=data, columns=columns)
print(df)


