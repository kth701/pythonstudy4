
# 다형성: 여러 가지 형태를 가질 수 있는 기능
# : 하나의 참조변쉬로 여러 타입(type)의 객체를 참조 할 수 있는 것

# 상속: 부모 클래스(공통기능) , 자식 클래스(공통 기능 확장)

# 1. 상위클래스(부모, 슈퍼, 베이스)
class Fligt:
    title_name = "다형성"
    def fly(self):
        print('날다, fly원형 메서드')

# 2. 자식 클래스 : 비행기
class Airplane(Fligt):
    name = '비행기'

    # 상위 클래스로 부터 상속받은 기능을 재구성
    #함수 재정의(오버라이딩)
    def fly(self):
        print('비행기가 날다')


class Bird(Fligt):
    name = '새'
    def fly(self):
        print('새가 날다')

class PaperAirplane(Fligt):
    name = '종이비행기'
    def fly(self):
        print('종이 비행기가 날다')

print("-- 부모 클래스")
fligt = Fligt()
print( fligt.title_name)
fligt.fly()

print("-- 자식클래스: 비행기")
air = Airplane()
print( air.name, air.title_name)
air.fly()

print("-- 자식클래스: 새")
bird = Bird()
print( bird.name, bird.title_name)
bird.fly()

print("-- 자식클래스: 종이비행기")
parer = PaperAirplane()
print( parer.name, parer.title_name)
parer.fly()

print("--- 다형성 구현")
fligt2 = Fligt()

# 상위 클래스 객체 = 하위(자식)클래스 객체
fligt2 = air
fligt2.fly()

fligt2 = bird
fligt2.fly()

fligt2 = parer
fligt2.fly()
