# tuple: 리스트 유사, 수정,삭제 불가
# "(원소,....)" : 괄호 기호 표기

#리스트: [], 튜플: ()
t1 = (2,7,4,3,9)
print(t1, t1[1], len(t1), sum(t1), max(t1), min(t1))
print(sorted(t1))

t2 = (10,) # 원소가 1인경우
print(t2, type(t2) )

# 수정 불가
# t1[1] =100 # TypeError: 'tuple' object does not support item assignment

#t1.append(200) # error 
t1 += (20,) # tuple 원소1개인 경우 추가시
print(t1)
