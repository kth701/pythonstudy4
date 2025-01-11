
# 람다 함수
# 1. 일반 함수(함수명칭이 있는 선언적 함수)
# def Adder(x,y):
#     add = x + y
#     return add

# r1 = Adder(10,20)
# print('add=',r1 )

# 2. 람다 함수(익명함수)
# r2 = (lambda x,y: x+y )(10,20)
# print('rambda add=',r2)

# 스코프(scope): 변수의 범위 => 지역 변수, 전역 변수

# x = 50  # 전역변수(함수 밖에서 선언)
# def local_func(x):  # 지역변수
#     x += 50
#     print("함수 안에 있는 x=",x)

# local_func(100)
# print('함수 밖에서 있는 x=',x)

# print("-- 전역 변수")
# def global_func():
#     global x # 전역변수 지칭
#     x += 50
#     print("함수 안에 있는 x=",x)

# global_func()
# print('함수 밖에서 있는 x=',x)

# 재귀함수(Recursive function): 함수 내부에서 자신의 함수를 반복으로 호출
# 재귀함수는 반드시 종료하는 조건을 작성해야 함.
def counter(n):
    if n == 0:
        print(n, end = " ")
        return 0
    else :
        print(n, end=" ")
        counter(n-1) 

counter(3)

# 5!=> 5*4*3*2*1
def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1) # 5*fac(4)=>4*fac(3)=>3*fac(2)=>2*fac(1)
    
print(  fac(5)  )

