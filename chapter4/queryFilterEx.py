from pandas import DataFrame

data = [
    [1416, 1416, 2994, 1755],
    [6.47, 17.63, 21.09, 13.93],
    [1.10, 1.49, 2.06, 1.88]
]

columns = ["2018/12", "2019/12", "2020/12", "2021/12(E)"]
index = ["DPS", "PER", "PBR"]

df = DataFrame(data=data, index=index, columns=columns)
print(df)

df.filter(items=['2018/12'])
df.filter(items=["PER"], axis=0)

df.filter(regex="2020") #2020이라는 문자열 일부로 필터링

df.filter(regex="^2020") #2020으로 시작하는 문자열 패턴만 선택

df.filter(regex="R$", axis=0) #R로 끝나는 모든 패턴을 탐색
