# 제어문: 프로그램 흐름을 제어
# if, while , for 유사

# 단순 if, if else , elif문
# num = 10
# if num > 10:
#     print('num=',num)
#     print('조건이 참인 경우 처리되는 문장')

# print("다음문장")

# num1 = input("정수: ")
# num1 = int(num1) # 문자형 -> 정수형

# 단순 if
# if num1%2 == 0 :
#     print(num1,"짝수")

# if num1%2 == 1:
#     print(num1, "홀수")

# 2. if else 문
# if num1%2 == 0:
#     print(num1, "짝수")
# else:
#     print(num1, "홀수")

# 3. elif문
score = int( input('점수입력: ')) #점수입력
grade ='' # 점수에 따른 등급

if score >=85 and score <=100:
    grade='우수'
elif score>=70:
    pass
else:
    pass

