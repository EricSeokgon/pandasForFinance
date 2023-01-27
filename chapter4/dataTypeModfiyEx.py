import numpy as np
from pandas import DataFrame


def remove_comma(x):
    return int(x.replace(',', ''))


data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
    ["850", "900", "1,185"]
]

columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
df = df.applymap(remove_comma)
df = df.astype({'03/02': np.int64, '03/03': np.int64, '03/04': np.int64})
print(df.dtypes)
