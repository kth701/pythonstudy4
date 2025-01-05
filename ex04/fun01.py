# 파이썬: 모듈과 패키지형태로 라이브러리를 제공
# 모듈은 다수의 함수나 클래스(class)를 묶어서 
# 파일형식(*.py)으로 제공

# 함수 :  특정 기능을 수행하는 단위 프로그램
# 내장함수 : builtins라는 모듈

# 형식
# 1. import 모듈명 : import random
# 2. from 모듈명 import 함수명1, ...

# builtins모듈에 있는 함수
dataset = list(range(1,6))
print(dataset)

# len(), sum(), max(), min()... 내장함수는 import과정생략
print(f"len={len(dataset)}")
print(f"sum={sum(dataset)}")
print(f"max={max(dataset)}")
print(f"min={min(dataset)}")

# import가 필요한 함수(builtins모듈에 없는 함수)
# import statistics
# print("평균=",  statistics.mean(dataset))
# print("중위수=", statistics.median(dataset))
# print("표본 분산=",statistics.variance(dataset))

from statistics import variance, stdev
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))




