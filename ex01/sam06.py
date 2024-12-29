# 문자열 색인=> 리스트 구조형식
#   "012345"
s = "PYTHON"
print(s)
print(s[0], s[1], s[2], s[3], s[4], s[5]) # 인덱스싱
print(s[-6],s[-5],s[-4],s[-3],s[-2],s[-1])

# 슬라이싱(slicing)
# 문자열[인덱스번호], 문자열[시작:끝:증감값]
# print('문자열길이:', len(s))
print(s[0:4]) # start, end-1
print(s[:4]) # start:생략 => 0으로 설정
print(s[:])
print(s[::2])

# 우측기준
print(s[-1], s[-2])
print(s[-6:-1]) # start, end-1
print(s[-6:])

# print("*"*20)
list1 = [100,200,300]
list2 =["홍길동","홍길순"]
list3 = list1 + list2
print(list3)

list4 = [1,2,3] +[100] 
print(list4)

list5 = [ 1,2,3,[100,200],[10,20],['a','b'] ]
print(list5[0])
print(list5[1])
print(list5[2])
print("------")
print(list5[3])
print(list5[3][0],list5[3][1])
