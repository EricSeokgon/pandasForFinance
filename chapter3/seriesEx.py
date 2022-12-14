from pandas import Series
import numpy as np

# 시리즈 생성
# data = [10, 20, 30]
data = np.arange(5)
s = Series(data)
print(s)

# 두개의 문자열을 저장하는 시리즈 객체 생성

data = ["시가", "고가"]
s = Series(data)
print(s)

# 문자열과 정수형 타입을 하나의 시리즈로 만들면 전체 데이터가 object타입으로 관리
# object타입의 시리즈는 브로드캐스팅 기능을 활용한 수치 연산을 할수 없다.
# 시리즈에는 같은 데이터 타입을 저장하는 것이 좋음
s = Series(['samsung',81000])
print(s)