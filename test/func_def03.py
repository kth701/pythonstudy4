# def mul(*a): # 전달 받는 인자의 개수가 특정 개수로 정해지지 않을 경우
#     result = 1

#     #print(a, type(a))
#     for i in a:
#         result *= i 
#         #print(f"{i}까지 누승:{result}")
    
#     return result


# r1 = mul(3,4,100,20,3)
# print(r1)

# "**매개변수"=> 딕트 타입
# adult=[1,2,3,4,34], non_adult=[2,3,4,3]
# def group_by_age(**kwargs):
#     #print(  kwargs )
#     group = {"adult":[], "non_adult":[]}
        
#     for name, age in kwargs.items(): #kwargs.keys(), kwargs.values(), kwargs.items()
#         print(name, age)
#         if age>18:
#             # group["adult"] = group["adult"] + [name]
#             group["adult"] += [name] 
#         else:
#             group["non_adult"] += [name]

#     return group

# print( group_by_age(kim=25, jeong=16, a=17,b=20,c=30,d=45) )
# r1 = group_by_age(kim=25, jeong=16, a=17,b=20,c=30,d=45)
# print(r1)

# def test1(*a, **b):
#     print( len(a), len(b))

# test1(10,20,30, animal="ape", fruit="apple")

# 변수의 타입을 명시적으로 선언 추세
def test2(name:str, age:int):
    print(f"당신의 이름은 {name}, 나이는 {age}")

test2("홍길동",20)

def test3(nums:list)->float:
    return sum(nums)**0.5

r1 = test3([1,2,3,4,5])
print(r1)

# 람다 함수
eq = (lambda a,b: a+b)(10,20)
print(eq)

eq2 = lambda a,b,c : "{}x+{}y={}".format(a,b,c)
print( eq2(5,4,3) )
# 실행 print(  "{}x+{}y={}".format(5,4,3) )


test3 = lambda x: "/".join(x)
print( test3(["apple", "banana","grape"]) )

def test4(x):
    t = "/".join(x)
    #print(t)
    return t

r1 = test4(["apple", "banana","grape"])
print( r1 )


