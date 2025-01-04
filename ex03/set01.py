# 비순서 자료구조: set, dict
# Set: 중복불가, 순서가 없다, 색인없다, 추가,삭제, 집합 연산 등 가능


# s = {1,3,4,3,1}
# print(s, len(s), type(s))

# for d in s:
#     print(d, end=", ")

# print()


# 집합 연산
# s2 = {3,6}
# print('s=',s, ' s2=',s2)

# print(s.union(s2)) # 합집합
# print(s.difference(s2)) #차집합
# print(s.intersection(s2)) #교집합

# 추가
# s.add(10)
# print(s)

# 삭제
# s.discard(10)
# print(s)

# 중복허용하는 리스트 객체
gender = ['남','여','남','여']

sgender = set(gender) # list구조 -> set구조 전환
lgender = list(sgender) # set구조 -> list구조

print(gender, lgender)

