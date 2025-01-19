
class XY:
    def __init__(self, x,y):
        # __변수 => 외부에서 접근불가능
        self.__x = x
        self.__y = y
    
    # getter기능
    # 함수의 데코레이터 기능을 활용하여 인스턴스 변수 접근 
    @property # 함수이름을 멤버변수이름처럼 사용
    def x(self):
        return self.__x
    
    #동일 한 이름의메서드에 .setter붙인 데코레이터: setter기능
    @x.setter
    def x(self, value):
        if value < 0:
            print("Wrawrnng : value < 0")

        self.__x = value
    
c = XY(3,4)
print(c.x) # c.x() => x()함수 이름을 x변수로 사용

# c.x = 30  # x함수이름 , 멤버변수 아님
c.x = 300   # c.x(300) 기능
print(c.x)