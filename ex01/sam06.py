# 문자열 색인=> 리스트 구조형식
s = "PYTHON"
print(s)
print(s[0],s[1],s[2],s[3],s[4],s[5])

# 슬라이싱(slicing)
# 문자열[인덱스번호], 문자열[시작:끝:증감값]
print('문자열길이:', len(s))
print(s[0:4]) # start, end-1
print(s[:4])
print(s[:])
print(s[::2])

# 우측기준
print(s[-1], s[-2])
print(s[-6:-1]) # start, end-1
print(s[-6:])

print("*"*20)
list1 = [100,200,300]
list2 =["홍길동","홍길순"]
list3 = list1 + list2
print(list3)

# list4 = [1,2,3] +100 # type error 
