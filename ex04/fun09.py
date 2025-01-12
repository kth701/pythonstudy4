# 함수 장식자: 데코레이터(decorator)
# : 함수의 기능을 변경하거나 확장할 경우

# 레퍼 함수
def wrap(f): # hello()함수의 주소가 인자로 전달
    def new_decorated():
        print('방가워요') # 시작 부분
        f() # hello()함수를 지칭
        print('잘가요') # 종료 부부

    return new_decorated # return하면서 new_decorated()자동 호출

# 함수 장식 적용
@wrap
def hello():
    print('Hello !!!!','홍길동')


# 함수 호출
hello()


print("-"*20)
def deco(f): #f에 hi()함수주소 전달
    def new_f():
        print("f() is called")
        return f() # return hi()
    
    return new_f

@deco
def hi():
    print("Hi....")

hi()

print("-"*20)


def func_with_print(f): # double()함수 주소 전달
    def new_func(x):
        print("double()함수 실행 전 처리하는 내용")
        y=f(x) # y = double(x) 수행
        print(y)
        print("double()함수 실행 후 처리하는 내용")
        return y
    return new_func #  new_func(5)함수를 실행한다는 의미

@func_with_print
def double(x):
    return 2*x

r1 = double(5) # double()함수 실행하면 인자값 5전달
print(r1)





