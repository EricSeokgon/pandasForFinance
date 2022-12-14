import numpy as np

# ndarray와의 연산은 브로드캐스팅이 적용되어 전체 데이터에 연산이 반복 적용됨
arr = np.array([10, 20, 30])
print(arr > 10)

# 인덱스의 리스트로 슬라이싱한 것과 유사하게 True와 False가 담긴 ndarray로 조건이 참인 데이터만 슬라이싱할 수있다.
arr = np.array([10, 20, 30])
cond = [False, True, True]
print(arr[cond])

# 두개의 조건을 비교하는 예제
arr = np.array([10, 20, 30])
cond0 = arr > 10
cond1 = arr < 30
print(arr[cond0 & cond1])

# 연산자 우선순위가 대소 비교보다 &가 높기 때문에 대소 비교 연산을 먼저 수행하기 위해 괄호로 조건을 반드시 묶어야 한다.
arr = np.array([10, 20, 30])
print(arr[(arr > 10) & (arr < 30)])

# 조건이 10이상이 값을 크다는 으미로 1 그렇지 않은 경우 0으로 매핑
arr = np.array([10, 20, 30])
cond = arr > 10
arr[cond] = 1
arr[~cond] = 0
print(arr)

# 넘파이에서는 where함수가 정의돼 있어서 이르 ㄹ사용하면 더욱 간단히 코드를 표현할 수 있다.
arr = np.array([10, 20, 30])
arr = np.where(arr > 10, 1, 0)
print(arr)

# 10보다 크다면 10을 더하고 그렇지 않다면 10을 빼기
cond = arr > 10
arr[cond] = arr[cond] + 10
arr[~cond] = arr[~cond] - 10

arr = np.where(arr > 10, arr + 10, arr - 10)
