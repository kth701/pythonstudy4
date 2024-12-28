# 표준 입력 장치(키보드), 표준 출력 장치(모니터)
# 외부장치로부터 넘어온자료는 스트림구조 : 문자열

# num = input("숫자 입력:") # 10,  10.25
#print(num, num*3, type(num))
#print(int(num)*3) # 정수 문자형 -> 정수형 변환
# print(float(num)) # 실수 문자형 -> 실수형 변환

print('n1=',10, 100+20)
print("010","1234","5678", sep=',')
print("010","1234","5678", sep='\n') # enter key
print("-"*10)

# 1. format(): 형식이 있는 출력: %f, %d, %o,%x, %s,%c
print('원주율=', format(3.14159,"8.2f"))
print('금액=', format(10000, "3,d") )


# 2.
name = "홍길동"
age = 35
price = 125.456

print("당신의 이름은 %s이고, 나이는 %d세입니다. 가진돈은 %.2f원입니다." 
        % (name, age, price) )

# 3.
print("이름: {2}, 나이: {1}세, 가진돈 {0}원".format(name, age, price))

# 4.
str1 = f"이름: {name}, 나이:{age}, 금액:{price}"
print(str1)

m = """\
this is
multi line
string\
"""

print(m)