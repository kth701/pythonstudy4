# 생성자 : "__init__" 생성자 함수 이름

class Number:
    # 생성자(특수 함수): 객체가 생성되는 시점에 자동호출
    # 객체가 생성하는 시점에 멤버변수에 초기값 설정
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 일반 함수
    def set_num(self, n):
        self.num = n

    # 매직 함수
    def __add__(self, n1):
        print("__add__()함수 호출")
        return self.num + n1

num1 = Number('홍길동',10)
print(num1.name, num1.age)

num1.set_num(3000)
print(num1.num)

# print( num1.__add__(100) )
print( num1 + 300) 



