
# 가변 인자 함수
# "*", "**" 기호를 붙여 사용
# "*매개변수"=>tuple, "**매개변수"=> dict

# def fun1(name, *names):
#     print(name)
#     print(names)
#     for n in names:
#         print(n)

# fun1("홍길동","홍길순","동길이","강감찬","이순신")

# 첫번째 인자는 n1, 나머지 인자는 n2에 전달(tuple구조)
# default=> 전달받은 값이 없을 경우 기본값으로 설정
# def mysum(n1=0, *n2):
#     sum = 0 
#     sum += n1   # sum = sum + n1

#     for n in n2: #2, 3, ....
#         sum += n    # sum = sum + n =>( +2,+3,...)

#     print("mysum=",sum)

# mysum(1,2,3)
# mysum(1,2)
# mysum(1,2,3,4,5)

# mysum() # 전달하는 인자값이 없으면 기본값이 적용됨


# def mycalc(num1=100, num2=200):
#     print(num1, num2)

# mycalc()
# mycalc(1000)
# mycalc(1, 2)

# 딕트형 가변인수
def emp_func(name, age,  **other):
    print(name)
    print(age)
    print(other)
    print("-"*10)
    print(other['addr'],other['height'],other['weight'])

    for k in other: # key값을 순차적으로 호출
        print(other.get(k)) # 객체.get(key) => value값을 호출

emp_func('홍길동', 35, addr='서울',height=178, weight=65)


