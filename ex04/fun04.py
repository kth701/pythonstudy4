# 사용자 정의 함수

# def 함수이름():
#     수행할 내용

# 1. 기능 수행하는 단순 함수: 매개변수 없고, 반환 값 없는 형태
# 함수 선언
# def fun1():
#     print("*"*10)
#     print('전달 받은 인자가 없고 반환값없는 함수')
#     print('Fun1()')
#     print("*"*10)

# 함수 호출(실행)
# fun1()


# 2. 기능 수행하는 단순 함수: 매개변수 있고, 반환 값 없는 형태
# def fun2(name):
#     print("-"*20)
#     print("안녕하세요. ",name,"님 !!!")
#     print("-"*20)

# fun2("홍길동")
# fun2("동순이")
# fun2("강감찬")

# 3. 기능 수행하는 단순 함수: 매개변수 있고, 반환 값 있는 형태
# def fun3(x,y):
#     print("사칙연산 함수 수행")
#     tot = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return tot, sub, mul, div

# 함수 실행
# a,b,c,d = fun3(10,3)
# print(a,b,c,d)

# 피타코라스의 정의 함수 만들기
# def pytha(s,t):
#     a = s**2 - t**2
#     b = 2 + s * t
#     c = s**2 + t**2

#     print("3변의 길이: ", a ,b,c)
#     return a,b,c

# a1,b1,c1 = pytha(2,1)
# print("함수반환값:",a1,b1,c1)

# def mysum(start, end):
#     sum = 0
#     for i in range(start, end+1):
#         sum += i # +i..

#     return sum

# print( mysum(1,10))
# print( mysum(1,100))
# print( mysum(5,10))


# 오버로딩 기능 지원 문제 발생
# def a():
#     print("hello")
# def a(name):
#     print(name)
# def a(n1,n2):
#     print(n1,n2)





