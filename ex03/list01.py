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


