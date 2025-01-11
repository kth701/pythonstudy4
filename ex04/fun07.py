# 함수의 객체화(주소개념)

# def mul(a,b):
#     return a*b

# mul2 = mul # mul주소를 mul2에 저장
# print( id(mul2), id(mul))
# print( mul2(3,4))

# 매개변수 -> 인자값(데이터), 함수식(함수의 주소)도 전달 가능
# def func01(f): # f에는 func02함수의 주소를 넘겨받음
#     print( "f(2,3)={}".format( f(10,20) ))

# def func02(a,b):
#     return a*b

# r1 = func02(10,20)
# r2 = func02
# print(r1, r2(100,200),  id(func02), id(r2))

# func01( func02 ) #  함수의 주소를 인자값으로 전달

def func03():
    def new_func03(a,b):
        #  return의미는  new_func03()함수를 종료
        return a*b
    
    # return의미는 func03()함수를 종료
    return new_func03 # new_func03()함수 주소를 가지고 반환

m = func03() # m에는 new_func03()함수의 주소를 저장
print( m(10, 20) )

# 중첩함수에서 외부함수나 내부함수를 변수에 저장 
#   => 일급함수(First class Function)
# 내부함수는 외부함수의 return명령문을 이용하여 반환  
#   => 함수 클로저(Function cloure)