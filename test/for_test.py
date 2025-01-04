# for문, while문
# for 변수 in iterable:
    # 수행할 반복 구간
    # ...

# for c in "apple":
#     print(c)
#     print("--")

# for n in [0,1,2,3]:
#     print(n, end=" - ")

# for i in range(3): # 0,1,2
#     print(i)
# for i in range(1,3): # 1, 2 (3은 포함되지 않음)
#     print(i)

# for  i in range(1,10+1):
#     print(i)

# for num in range(1, 100+1):# 1~100까지 반복
#     if num%10 == 0:
#         print(num, end = ",")

# 값이 있는 리스트 객체
files = ["apple.jpg","banana.png","names.txt","grape.jpg","profiles.txt"]
jpgs = [] # 비어 리스트 객체

# [1,2,3] +[5] => [1,2,3,5]
# [1,2,3] +"abc" => type error 

# for f in files:
#     print(f, f[-4:])

#     if f[-4:] == '.jpg': # 확장자기 '.jpg' 조건만 처리
#         jpgs += [f] # jpgs = jpgs + [f]

# print(jpgs)

list1 = []

# print([1,2,3]+[10])
# print([1,2,3] + 10) # error

# list1 = list1 + [1,2] # [] + [1,2]
list1 += [1,2]

print(list1)





 