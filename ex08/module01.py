#  파일단위 저장된 클래스 및  함수

# 변수1개, 함수 3개 포함된 모듈
PI = 3.141592

def number_input():
    #키보드로 데이터 입력
    output = input("숫자 입력>") 

    # 문자열 => 숫자형
    return float(output)

def get_circumference(radius):
    return 2*PI*radius

def get_circle_area(radius):
    return PI*radius*radius

if __name__ == "__main__":
    print("== 현재 모듈 이름")
    print(__name__)
    print("-----")