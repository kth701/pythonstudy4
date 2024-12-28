# 대입연산자: +,=,*,/,... => +=, -=,*=, /=,...
i = tot = 10
print(i, tot)

i += 1   # i = i + 1
print(i) # 11

i += 1  # 12
print(i)

i += 1  # 13
print(i)

i *= 3 # i = i * 3
print(i) 
i /= 2  # i = i / 2
print(i)

v1, v2 = 100, 200
print(v1, v2)

v1, v2 = v2, v1
print(v1, v2)

# 변수 : 단일 기억장소
# 리스트 구조 : 여러개의 데이터를 순차적으로 보관
list1 = [1,2,3,4,5]
print(list1, list1[0], list1[1])

v1, *v2 = list1
print(v1, v2)

*v1, v2 = list1
print(v1, v2)

