# excel 파일 처리
import pandas as pd

# excel파일 열기
sam = pd.ExcelFile('sam_kospi.xlsx')

# excel 파싱
kospi = sam.parse("sam_kospi")
print(kospi.info())

# 컬럼 추출
high = kospi['High']
low = kospi['Low']

from statistics import mean
# 평균
print('high mean= ', mean(high), high.mean())
print('low mean = ', mean(low), low.mean())

