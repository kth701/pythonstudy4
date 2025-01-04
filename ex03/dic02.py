test = {}
print(test.get('name', 0))

test['name'] = test.get('name',0)
print(test)

test['name'] = test.get('name',0)+1
print(test)

test['name'] = test.get('name',0)+1
print(test)



# 단어 빈도수 구하기
# charset = ['abc', 'code','band','band', 'abc']

wc = {} # Set, Dict
for key in charset: #리스트 객체
    # print(key, wc.get(key), wc.get(key, 0))

    wc[key] = wc.get(key, 0)+1
    #wc['abc'] = wc.get('abc',0)+1
    print(wc)

print('-'*20)
print(wc)
    