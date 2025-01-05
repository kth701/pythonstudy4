#  자주 쓰이는 표현식
# names = ["홍길동", "동순이","길동이"]
# # n1 = "/".join(names)
# n1 = "".join(names)
# print(n1, type(n1), len(n1))

# input =>문자형 => 계산목적 => int(), float()
# num1 = int( input("숫자입력:") )

# isEvenOrOdd = "짝수" if num1%2==0 else "홀수"
# print(f"입력받은 숫자는 {num1}는(은) {isEvenOrOdd}")

# -------------------------------------------- #
# 리스트 컴프리헨션: list안에 for, if문
# -------------------------------------------- #

# 1.
s1 = []
for i in range(5):
    # print(str(i), type(str(i)))
    s1.append( str(i )) # 숫자 -> 문자 -> list 추가
print(s1)

# 0->'0'전환해서 list에 저장
str1 = [str(i) for i in range(5)] 
print(str1)

print("-"*20)

# 2.
s2 = []
for i in range(1, 10+1):
    if i%2 == 0: # 짝수인 숫자만 -> 문자로 저환
        # print(str(i), end="\t")
        s2.append( str(i) )
print(s2)

n2 = [str(i) for i in range(1,10+1) if i%2==0]
print(n2)

# 3.
# for i in [1,2,3]: # i=1,2,3
#     for j in [10,20,30]: # j=10,20,30
#         print(i, j)

a = []
for i in ["slow","fast"]: # i= "slow", "fast"
    for j in ["dog","cat"]: # j = "dog", "cat"
        a.append("{} {}".format(i,j)) # (slow dog),....
        print(i,j)
print(a)

n3 = [ "{} {}".format(i,j) for i in ["slow","fast"] for j in ["dong","cat"]]
print(n3)
