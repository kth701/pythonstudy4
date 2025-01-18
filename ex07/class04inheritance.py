# 상속(Inheritance): 코드의 재사용과 다형성
# 부모클래스(슈퍼클래스, 상위클래스) : 공통 기능을 가진 클래스
# 자식클래스(하위클래스, 파생클래스) : 공통 기능을 확장하는 클래스

# 부모 클래스(공통 기능)
class Super:
    def __init__(self,name, age):
        print('부모클래스 생성자 호출')
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name}, age: {self.age}")

# 부모 클래스로 객체 생성
sup = Super('부모 클래스', 55)
sup.display()



print("-"*20)
# 하위클래스 (공통 기능 확장)
class Sub(Super): #클래스(부모클래스이름) => 상속개념
    gender = None

    def __init__(self, name, age, gender):
        #상위클래스 멤버변수 초기화 : 생성자호출 =>  super()
        super().__init__(name, age)
        print('자식클래스 생성자 호출')

        # gender 자식 클래스의 자원
        self.gender = gender

    # 오버라이딩(상속 받은 메서드 재정의)
    def display(self):
        print(self.name, self.age, self.gender)

# 자식 클래스 객체 생성
sub = Sub('자식 클래스', 25, '여자')
print("-- sub display()")
sub.display()

print("--- sub 클래스 멤버변수")
print(sub.name, sub.gender, sub.age)


