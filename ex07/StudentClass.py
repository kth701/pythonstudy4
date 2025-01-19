# 학생

class Student:
    # 생성자 : 멤버변수 초기값 설정
    def __init__(self, name, kor, mat, eng, sci):
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng
        self.sci = sci

    # 기능 수행 함수 선언
    def total(self):
        return self.kor+self.mat+self.eng+self.sci
    
    def average(self):
        return self.total() / 4
    
    def to_string(self):
        return "{}\t{}\t{:.2f}".format(self.name, self.total(), self.average())
    
    # 특수 함수
    def __str__(self):
        return "{}\t{}\t{:.2f}".format(self.name, self.total(), self.average())



if __name__ == "__main__":
    students = [
        Student("홍길동", 100, 100, 100,100),
        Student("동순이", 80, 75, 65,85),
        Student("길순이", 90, 75, 65,60),
    ]   

    print("이름\t총점\t평균")
    for st in students:
        # print( st.to_string() )
        print( str(st) )
    