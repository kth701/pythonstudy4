
# 자료 구조 복제: 얕은 복사, 깊은 복사
print("-- 객체 주소 복사")
print("1. 얕은 복사: 주소복사")

name = ['홍길동','이순신','강감찬']
print(f"name={name}")

# name2에 name이 담고있는 객체 주소를 저장
name2 = name
print(f"name2={name2}")

print(f"name주소:{id(name)}, name2주소:{id(name2)}")

# 복사본을 수정
name2[0] = "길순이"
print(f"name={name}")
print(f"name2={name2}")

print("-"*20)

# 깊은 복사
import copy
print("2. 깊은 복사")
name3 =  copy.deepcopy(name)

print(f"name={name}, name3={name3}")
print(f"name주소={id(name)}, name3주소={id(name3)}")

name3[0] = "동순이김"
print(f"name={name}, name3={name3}")