
class XY:
    def __init__(self, x,y):
        # __변수 => 외부에서 접근불가능
        self.__x = x
        self.__y = y
        self.name = "동순이"
    
    @property # 함수이름을 멤버변수이름처럼 사용
    def x(self):
        return self.__x
c = XY(3,4)
print(c.x) # c.x() => x()함수 이름을 x변수로 사용


c.name ="길순이"
# c.x = 30  # x함수이름 , 멤버변수 아님