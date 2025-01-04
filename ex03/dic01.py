# 딕트(dict): 키중복 불가, 값은 중복가능, 키로 통해 값을 호출
# 리스트 = [1,2,3] 튜플 =(1,2,3), 셋={1,2,3}
# 딕트 = {'a': '1',...}

# 1. 생성자로 통해 값설정 :  키=값,...
dic = dict(key1=100, key2=200, key3=300)
print(dic, type(dic))

# 2. 초기값 설정: 키:값,...
person = {'name':'홍길동','age': 35, 'addr':'부산시'}
print(person, type(person))

# 3. key로 value호출(참조)
print(person['name'], person.get('age'))

# 4. 추가/수정
person['name'] = '동순이' # 수정
person['age'] = 10
person['gender'] = '여자' # 추가
print(person)

# 5. 삭제
del person['gender']
print(person)

# 6. 유무 체크
print( 'age' in person, 'gender' in person)


# 7. 반복
for key in person.keys(): #키만 추출
    print(key, person.get(key))

for value in person.values():# 값만 추출
    print(value)

for item in person.items(): # 키와 값 추출
    print(item, item[0], item[1]) # 튜플 형식으로 키와 값 구성

# print(person.keys(), person.values())
# print(type(person.keys()), type(person.values()))

# dict구조 : 값 호출 => dict객체['키이름'], 
# dict객체.get('키이름'), dict객체.get('키이름', 키가 없을 경우 설정할 값)

print('-'*20)
print(person)
print(person['name'], person.get('age'), person.get('gender', '남자'))


