#  builtins 내장함수

print(abs(10), abs(-10))
# 모든 요소가 True => True => and유사 기능
print( all([1,True, 10, -15.2]) )
# False인 데이터: "", [],{},0
# print( all([1,True, 10, -15.2, 0]) ) 
# print( all([1,True, 10, -15.2, ""]) ) 
# print( all([1,True, 10, -15.2, []]) ) 

# 하나 이상의 요소가 True => True: OR유사
print("-- any()")
print( any([0,"", [],{}]) )
print( any([0,"", [],{10}]) )

print(10, bin(10), hex(10), oct(10))
# "10+20" => 10+20
print(eval("10+20"))

# 문자의 아스키코드 번호
print(ord('A'),ord('a'))

print(pow(3,2))# 3의 2승
print( sorted([4,2,1,8,5]))
