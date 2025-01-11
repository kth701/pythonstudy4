
# 함수: 특정 기능를 수행하는 코드의 나열
# 기능을 수행하는 함수 선언(작성) -> 함수 호출(실행)

# 함수 선언
# def calc_area():
#     print('Hello')
#     print('안녕')
#     print('calc_area()함수')

# calc_area() # 함수 호출
# calc_area()
# calc_area()

# 인자값 있고, 반환값 없는
# def calc_area(h, w):
#     area = h * w
#     print('height:', h)
#     print('width:', w)
#     print('area:', area)

# calc_area(5,4)

# 인자값 있고, 반환 값
# def calc_area(h,w):
#     area = h * w
#     return area # 값을 반환

# result = calc_area(5,4)
# print(result)

# 특정 범위 숫자 출력하는 함수 선언
def print_number(start, end):
    if start > end:
        start, end = end ,start

    for i in range(start, end+1):
        print(i, end =" ")


print_number(10,5)