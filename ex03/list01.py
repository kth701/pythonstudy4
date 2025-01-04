#  자료 구조: 데이터(객체)가 메모리에 배정될 때 기억공간에 적재되는 구조
# 순서 자료구조: 리스트, 스트링(문자열), 튜플
# 비순서 자료구조: 딕셔너리

# lst1 = [ 100, 200,300,400,500]
# print(lst1, lst1[0], lst1[1])
# print(lst1[0:3], lst1[:3])
# print(lst1[-3:-2], lst1[-3:])

# 리스트에 데이터 추가: append()
# lst1.append(1) # 데이터 추가
# print(lst1) 

# lst1.append(["홍길동","홍길순"])
# print(lst1) 
# print(lst1[5],lst1[6], lst1[6][0], lst1[6][1])

# 데이터가 있는 인덱스 번호 추출
# print(lst1.index(100), lst1.index(500), lst1.index(7))

# 리스트: append(), insert(), remove()
# num = ['one','two','threee','four']
# print(num, len(num))

# 추가
# num.append('five')
# print(num, len(num))

# 삭제
# num.remove('five')
# print(num, len(num))

# 수정
# num[3] = '4'
# print(num, len(num))

# 삽입(추가)
# num.insert(3, 'zero')
# print(num, len(num))

# 제거: pop(인덱스번호)
# num.pop(0)
# print(num, len(num))

# 리스트 데이터 모두 제거
# num.clear()
# print(num, len(num))


# lst = [1,2,3,4,5]
# print(lst, type(lst))

# for i in lst:
#     print(lst[:i])

# print( 5 in lst) # 값을 포함하고 있으면 True판별
# print( 5 not in lst) #값을 포함하고 있지 않으면 True

# 리스트 내포(list안에 for와 if문)

x = [2,4,1,5,7]
lst = [i**2 for i in x]
print(x, lst)

# temp = []
# for i in x:
#     temp.append(i**2)
#     print(temp)
#     print("----")

# print(temp)

#조건에 부합한 데이터만 처리
lst2 =[ i*2 for i in x if i%2 == 0]
print(lst2)




