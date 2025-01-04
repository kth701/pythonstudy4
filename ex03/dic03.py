dic = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","치자황색소"],
    "origin":"필리핀"
}

for key in dic.keys():
    print(key, dic.get(key))

    # 값의 형식이 List이면 처리
    # if  type(dic.get(key)) == type([]): 
    if isinstance(dic.get(key), list):# 자료형 타입이 list이면 처리
        print("-----")
        for i in dic.get(key):
            print(i, end=" ")
        print("\n-----")


    
 