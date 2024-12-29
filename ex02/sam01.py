
#문자열 처리 함수
# 1. 특정 글자 수 반환
str1 = "this is one line string"
print('길이:',len(str1))
print('t 글자수:', str1.count('t'))

# 특정 문자 비교 판단
print(str1.startswith('this')) # True
print(str1.startswith('that')) # False

# 특정문자 교체
print( str1.replace('this','that') )
print( str1.replace(' ','')) # 공백 제거

# 문자열 분리
str2 = """\
홍길동
여러줄을 사용하기
길순이 동길이\
"""
print(str2)
sent = str2.split('\n') # 특정 문자기준으로 분리해서 리스트구조 저장
print('sent=',sent)

sent2 = ",".join(sent)
print(sent2)

# \', \", \\ : c:\abc\ttt.txt
print("홍길동\t홍길순\t동\\길이")
# sent = str2.split(' ')
# print(sent)

# 특정문자 포함여부 판별
print("안녕" in "안녕하세요")
print("Hello" in "안녕하세요")
print(1 in [1,2,4,5] )  # True
print([1] in [1,2,4,5]) # False
print([1] in [1,2,4,5, [1] ]) # True
