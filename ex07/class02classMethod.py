
# 클래스 멤버 : 클래스이름으로 호출할 수 있는 클래스변수, 클래스 메서드
# 칠래스 메서드는 'cls'기본 인수사용, @classmethod라는 함수 장식자 사용

class DatePro:
    # 클래스 멤버변수 => 클래스이름.변수 로 접근이 가능
    const = "날짜 처리 클래스"

    def __init__(self, year, month, day):
        # 생성자에서 self.변수 => 객체.변수 => 객체이름.변수형식으로 접근
        self.year   = year
        self.month  = month
        self.day    = day

    def display(self):
        print(f"{self.year}-{self.month}-{self.day}")

    # 클래스 메서드
    @classmethod
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month =dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")


date = DatePro(2025,1,18)

# date 객체이름으로 멤버변수, 멤버메서드(함수) 접근
print(date.year, date.month, date.day)
print(date.const)
date.display()

# ---------------------------------------- #
# 클래스이름으로 접근 불가능
# ---------------------------------------- #
# DatePro.year
# DatePro.display()
# ---------------------------------------- #

# 클래스 멤버 : 클래스이름.멤버변수
print( DatePro.const)
DatePro.date_string('20300118') #클래스이름.메서드(함수)명 접근 가능

# 클래스 변수, 메서드는 객체이름로 접근이 가능
date.date_string('20300118')
print(date.const)
