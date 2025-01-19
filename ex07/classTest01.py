# 클래스: 변수 + 함수

#클래스안에 있는 함수: self인자가 있으야 한다.
#클래스안에 있는 변수: self.변수
#클새스 생성자: 생략시, python이 기본값으로 자동 생성

class XY:
    #멤버변수 => 클래스 멤버변수
    name = 'hong' 
    def set_xy(self, x,y):
        # self.변수 => 인스턴스 변수
        # self.x :  현재 클래스안에 선언되는 변수 => 멤버변수
        self.x = x
        self.y = y

# XY클래스 구조를 생성자로 통해 객체를 생성: 인스턴스, 참조형, 객체
obj1 = XY() 
obj1.set_xy(100,200)

obj2 = XY()
obj2.set_xy(10,20)

print(id(obj1), id(obj2))
print(obj1.x, obj1.y, obj1.name, XY.name)
print(obj2.x, obj2.y)

