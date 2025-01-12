# 정규 표현식(Regular Expression)
# 특정한 규칙을 가진 문자열의 집합을 표현, 문자열 검색, 치환 용도로 사용
# 메타문자
# . => .x 또는 x. : 임의의 한 문자가 x앞에나 뒤에 오는 패턴 지정
# ^ => ^x : x로 시작하는 문자열
# $ => x$ : x로 끝나는 문자열
# "*" : x* : x가 0번 이상 반복
# + => x+ : x가 1번 이상 반복
# "?" => x?  : x가 0 또는 1개 존재
# | => abc|ABC : abc 또는 ABC
# [] => [x] : x문자 한 개일치
# [^] => [^x] : x문자 제외
# {n}, {n,}, {n,m} => x{n} : x문자가 n반복

import re 
# from re import finall 

st1 = '1234 abc홍길동 ABC_555_6 _만세1234 이사도시'

# 숫자 찾기
# print( re.findall('1234', st1))
# print( re.findall('[0-9]',st1))
# print( re.findall('[0-9]{3}', st1))
# print( re.findall('[0-9]{3,}', st1))
# print( re.findall('\\d{3,}', st1))

# 문자열
# print(st1)
# print( re.findall('[가-힣]{3,}', st1))
# print( re.findall('[a-z]{3}', st1))
# print( re.findall('[a-zA-Z]{3}', st1))
# print( re.findall('\\w{3}', st1))

# 특정 위치의 문자열 찾기
st2 ='test1abcABC 123mbc 456test'
print(st2)
print( re.findall('^test', st2))
print( re.findall('st$', st2))

print( re.findall('.bc', st2)) # 한문자에 대한 와일드 문자
print( re.findall('t.', st2))

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(st3)
words = re.findall('\\w{3,}', st3)
print(words)

words2 = re.findall('[^^*$]+', st3) # 특수문자 제외
print(words2)

