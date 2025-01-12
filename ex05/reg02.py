# 문자열 검사 예문
from re import match, sub

# 1. 패턴과 일치된 경우
jumin = '121112-1234567'
result = match('[0-9]{6}-[1-4][0-9]{6}',jumin)
print(result)

if result:
    print('주민번호 일치')
else:
    print('잘못된 주민번호')

jumin2 = '121112-5234567'
result2 = match('[0-9]{6}-[1-4][0-9]{6}',jumin2)
print(result2)

if result2:
    print('주민번호 일치')
else:
    print('잘못된 주민번호')

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
# 특수문자 제거 => 치환기능 => "기존문자","바꿀문자"
print(st3)
text1 = sub('[\^*$]+', '',st3)
print( text1 )

text2 = sub('[0-9]','',st3)
print( text2 )





