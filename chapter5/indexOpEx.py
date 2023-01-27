import pandas as pd

idx1 = pd.Index([1, 2, 3])
idx2 = pd.Index([2, 3, 4])
print(type(idx1))

idx1.union(idx2) # 합집합

idx1.intersection(idx2) # 중복된 데이터만 선택하고 싶다면 intersection 메서드를 사용한다. 교집합

idx1.difference(idx2) # idx1에서 idx2와 중복되는 인덱스 값만 제거하고 싶을때 집합에서 차집합과 같다.