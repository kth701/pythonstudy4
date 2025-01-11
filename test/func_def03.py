def mul(*a): # 전달 받는 인자의 개수가 특정 개수로 정해지지 않을 경우
    result = 1

    #print(a, type(a))
    for i in a:
        result *= i 
        #print(f"{i}까지 누승:{result}")
    
    return result


r1 = mul(3,4,100,20,3)
print(r1)

# "**매개변수"=> 딕트 타입`
def group_by_age(**kwargs):
    print(  kwargs )

group_by_age(kim=25, jeong=16)

