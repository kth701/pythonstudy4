# 실수 -> 정수 : int(실수형)
a = int(10.5)
b = int(20.42)
add = a + b
print('add= ', add)

# 정수 -> 실수 : float(정수)
a1 = float(10)
b1 = float(20)
add1 = a1 + b1
print('add1= ', add1)

# 논리형 -> 정수
print( int(True), int(False))

# 문자형 -> 정수
st = '10'
# print(st+3)  type error``
print(int(st)+3)
