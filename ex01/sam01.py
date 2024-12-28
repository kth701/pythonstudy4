# 주석문
# 변수: 단일 기억장소
# 상수: 기억장소에 넣을 값(데이터)

# 대입문:  기억장소 = 값, 수식, 다른 기억장소값

a = 100
a = 200
print(a)

b=300+100-10
print(b)

c=b
print(c)

str1 = "홍길동"
str2 = "부산시"
str3 = str1 + str2
print(str1)
print(str2)
print(str3)

print("----")
print( id(a), id(b), id(c) )

print(a,type(a))
print(str1, type(str1))
print(type(10), type(10.245))
print(5>2, type(5>2), type(True), type(False))


# https://github.com/kth701/pythonstudy4








# 프로그램언어 : 명령어 집합
# 고급언어(파이썬,..), 저급언어(기계어,..)
# 번역실행방식: 컴파일러(오브젝트이있음), 인터프리터(줄단위, 오브젝트없음)
