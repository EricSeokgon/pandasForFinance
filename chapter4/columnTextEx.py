from pandas import DataFrame
import numpy as np

data = [
    {"cd": "A060310", "nm": "3S", "close": "2,920"},
    {"cd": "A095570", "nm": "AJ네트웍스", "close": "6,250"},
    {"cd": "A006840", "nm": "AK홀딩스", "close": "29,700"},
    {"cd": "A054620", "nm": "APS홀딩스", "close": "19,400"}
]
df = DataFrame(data=data)
df

