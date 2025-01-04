
# 단순 if
# if 조건식:
#     실행코드1
#     실행코드2
#     ....
# if문 벗어난 다음 문장

# num = 9
# if num >= 10:
#     num+=100
#     print(num)
#     print("조건이 참이면 수행중")

# print(" if문 다음 문장")

# if sum([1,2,3]) > 10:
#     print([1,2,3])
#     print("전체 합이 10보다 크다")
# print("out of if")

# if -3: # 0을 제외한 모든 숫자 True판별
#      print("참")

# if 0: #False
#      print("0은 참")

# if "홍길동": #True
#     print("문자 값이 있으면 참")
# if "": #False
#     print("텅빈 문자")
# if " ": #True
#     print("공백 문자")

# if [1,2,3]: #True
#     print("리스트에 값이 있음")
# if []: #False
#     print("리스트에 값이 없음")

# 중첩 if
# score = 61
# if score > 70: #True
#     print("score점수가 70이상입니다.")

#     if score%2 == 1: # 70이고 홀수인가 판별
#         print("홀수")

#키보드로 값을 입력 => 기본형이 문자형 => 숫자형변환(int(), float())
# num = int( input("숫자를 입력하세요. ") )
# if num%3 == 0 and num%6 == 0 :
#     print(f"{num}은 3의 배수이면 6의 배수입니다.")

# if num%3 == 0 or num%6 == 0 :
#     print(f"{num}은 3의 배수이거나 6의 배수입니다.")

# else문: if 참 else 거짓
# score = int( input("점수를 입력하세요: "))
# if score >= 60:
#     print("pass")
# else:
#     print("fail")

# 삼항 연산자
# print("pass") if score >= 60 else print("fail")

# num2 = 10
# if num2>0:
#     print("양수")
# elif num2 == 0:
#     print("0")
# elif num2 < 0:
#     print("음수")
# else:
#     print("기타")

# score = int( input("점수를 입력하세요: "))
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")
    







