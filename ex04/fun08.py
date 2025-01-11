# 일급함수와 함수 클로저

# 1. 일급함수
def a(): # outer function()
    print('a()함수: outer function')

    def b(): # inner function()
        print('b()함수:inner function')

    print('a()함수 종료시 b()함수의 주소를 반환')
    return b

# f1 = a()
# f1() # inner function b()함수가 실행

# 함수 클로저 예시
data = list(range(1,101))
print(data)

def out_func(data):
    dataSet = data

    def tot():
        tot_val = sum(dataSet)
        return tot_val
    
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val

    return tot, avg

# 외부 함수 호출(실행)
# total, average = out_func(data) # tot(), avg()함수의 주소를 반환

# tot_data = total()
# print('tot=', tot_data)

# avg_data = average(tot_data)
# print('avg=', avg_data)

def double(x):
    return 2*x

def func_with_print(f): # f에는 double()함수 주소
    def new_func(x):
        y = f(x) # => y = double(x)
        print(y)

        return y
    return new_func

# 함수의 주소 전달 받기
new_double = func_with_print(double)

# print( new_double(5) )

# 획득자와 지정자(getter, setter)
def main_func(num):
    num_val = num

    def getter():
        return num_val
    
    def setter(value):
        nonlocal num_val # 내부함수에서 외부함수에 선언된 변수가 사용시 설정
        num_val = value

    return getter, setter

getter, setter = main_func(100)

# getter()함수 실행
print( getter() )

# setter()함수 실행
setter(300)
print( getter() )

