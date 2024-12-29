# for 
str = "홍길동홍길순동길이"
# print(str)
# print( str[1] )

for name in str:
    print(name, end=" ")
print()

nums = [1,2,3,4,5,6,7,8,9,10]    
for n in nums:
    if n%5==0:
        print(n, end =" ")

print()
# for , rang:숫자 발생 객체
# n1 = range(5)        
# for n in range(5): # 0~4
# for n in range(1,5)  1~4
for n in range(1,10+1,2):    
    print(n, end =" ")

print()

# 난수 발생 모듈 임포트
import random
list1 = [[],[],[],[],[]] # 숫자 저장소

# ------------------------------- 
for out in range(5): # out:0-4
    # ------------------------------- 
    for i in range(6):
        r = random.randint(1,45) #1-45사이 난수 발생

        # 난수 발생후 저장소에 유무 체크
        while r in list1: # r값이 list1에 있으면 반복수행
            r = random.randint(1,45)

        list1[out].append(r) # 리스트에 저장
        print(r, end=" ")
    # ------------------------------- 
    print() #줄바뀜
# ------------------------------- 


print("-"*10)
for i in range(5):
    print(list1[i])