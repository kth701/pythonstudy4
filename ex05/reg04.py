# 자연어 전처리 예문
from re import findall, sub

# 더미 텍스트
texts = [
' 우리나라 대한민국., 우리나라%$ 만세',
'비타민&라 1000GRAM 분량',
'나는 대한민국 사람',
'보험료 15000원에 평생 보장 마감 입박',
'나는 홍길동?'
]

# 1단계: 소문자 변경
texts_re1 = [ t.lower() for t in texts]
print(texts_re1)

# 2단계: 숫자 제거
texts_re2 = [ sub("[0-9]","", text) for text in texts_re1]
print(texts_re2)

# 3단계: 문장부호 제거
texts_re3 = [ sub("[,.?!:;]","", text) for text in texts_re2]
print(texts_re3)

# 4단계: 특수문자 제거
texts_re4 = [sub("[@#$%^&*()]","",text) for text in texts_re3]
print( texts_re4)

# 4단계: 영문자 제거
texts_re5 = [''.join(findall("[^a-z]", text)) for text in texts_re4]
print(texts_re5)

# 4단계: 공백 제거
texts_re6 = [' '.join(text.split()) for text in texts_re5]
print(texts_re6)


