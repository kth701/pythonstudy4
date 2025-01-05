#  builtins 내장함수

# print(abs(10), abs(-10))
# 모든 요소가 True => True => and유사 기능
# print( all([1,True, 10, -15.2]) )
# False인 데이터: "", [],{},0
# print( all([1,True, 10, -15.2, 0]) ) 
# print( all([1,True, 10, -15.2, ""]) ) 
# print( all([1,True, 10, -15.2, []]) ) 

# 하나 이상의 요소가 True => True: OR유사
# print("-- any()")
# print( any([0,"", [],{}]) )
# print( any([0,"", [],{10}]) )

# print(10, bin(10), hex(10), oct(10))
# "10+20" => 10+20
# print(eval("10+20"))

# # 문자의 아스키코드 번호
# print(ord('A'),ord('a'))

# print(pow(3,2))# 3의 2승
# # [1,-3,5,4] => [1,3,5,4] => 정렬
# print( sorted([1,-3,5,4], key=abs))

# names =["BANANA", "GRAPE", "apple"]
# print(sorted(names))
# print( sorted(names, key=lambda x:x.lower()))

# nums = [[500,6], [10,20,30]]
# print(max(nums, key=len)) 
# print(max(nums, key=sum))

# n1 = [1,2,3]
# n2 = ["one","two","three"]
# # n3 = "abc" #n3[0],n3[1],n3[2]
# n3 = "abcdefg"

# # n1, n2각각의 요소를 튜플 방식 묶어줌
# for item in zip(n1,n2,n3): 
#     print(item)

# print("-"*10)

# names2 = ["홍길동","홍길순","동길이"]
# # for n in names2:
# #     print(n)

# for i, n in enumerate(names2, 100):
#      print(i, n)

# chars = ["*","+","#","&"]
# for i, c in enumerate(chars,1):
#      print(c*i) # i=0,1,2,3....

# 객체 타입 판별
print( isinstance(100, int), isinstance(10.2, int))
print( isinstance(100, float), isinstance(10.2, float))
print( isinstance(100, str), isinstance("10.2", str))
print( isinstance([1,2], list), isinstance((1,2), list))
print( isinstance([1,2], tuple), isinstance((1,2), tuple))
print( isinstance([1,2], dict), isinstance({"name":"hoing"}, dict))
print(type("abc"), type([]), type({1,2}), type((10,)), type({"age":10}))