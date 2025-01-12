
# 자연어 전처리 예문
from re import findall, sub

texts = [
' 우리나라 대한민국., 우리나라%$ 만세',
'비타민&라 1000GRAM 분량',
'나는 대한민국 사람',
'보험료 15000원에 평생 보장 마감 입박',
'나는 홍길동?'
]

# 테스트 전처리 함수
def crean_text(text):
    # 1-6 단계
    
    texts_re1 = text.lower()
    texts_re2 = sub("[0-9]","", texts_re1)
    texts_re3 =  sub("[,.?!:;]","", texts_re2) 
    texts_re4 = sub("[@#$%^&*()]","",texts_re3)
    texts_re5 = sub("[a-z]",'', texts_re4)
    texts_re6 = ' '.join(texts_re5.split())

    print(texts_re6)
    return texts_re6

# 함수 호출
texts_result = [crean_text(text) for text in texts]
print( texts_result )
