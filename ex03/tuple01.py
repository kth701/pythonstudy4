# 튜플(tuple): 읽기 전용(수정,삭제 불가)
# 색인, 슬라이싱, 연결, 반복, 요소검사 등 가능
# 리스트 보다 처리속도가 빠르다

# lst = [], lst[1], lst=[1,2,2,3,32]

# 1개인 경우("콤마기호가 접미로 붙여한다.")
t = (10,)
print(t, type(t))

t2 = (1,2,3,4,5,3,3,3,3,3)
print(t2, t2[0],t2[4], t2[1:4], t2[1:-6])
# 수정 불가
# t2[0] = 100 # error
for i in t2:
    print(i, end=' ')
    
print(100 in t2)
print(100 not in t2)

# lst = list(r) # range형식 -> list형식 전환
# print(lst)

r = list(range(1,5+1)) # range형식 -> list형식 전환
print(r, type(r))

t3 = tuple( r ) # tuple객체 생성
print(t3, type(t3))

#tuple에 있는 요소중 특정 데이터 개수
print(t3.count(3), t2.count(3), t2.index(3))




