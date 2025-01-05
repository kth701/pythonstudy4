# Set 중복제거
s1 = {1,1,1,1,1,1,1,1,1,1,1}
print(s1)

# 집합연산자: 합집합, 교집합, 차집합
set1 = {1,2,3,4,5}
set2 = {4,5}

print(f"set1={set1}, set2={set2}")
print(set1 | set2) # "|" set1.union(set2) 합집합
print(set1 & set2) # "&" set1.intersection(set2) 교집합
print(set1 - set2) # "-" set1.difference(set2) 차집합
print(set1 ^ set2) # "-" set1.symmetricdifference(set2) 대칭 차집합


list1 =[1,3,4,2,3,22,23,12,1,2,2,34,4,2]

set3 = set(list1) # list -> set (중복제거)
print(list1, set3) 

list2 = list(set3) # set -> list전환(중복제거된 list)
print(list2)