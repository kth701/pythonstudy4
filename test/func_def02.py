# def no_arg():
#     return 0
# def one_agr(a):
#     return a
# def two_arg(a,b):
#     return a+b

# print( no_arg())
# print( one_agr(5))
# print( two_arg(3,4))

# def lin_eq(a,b,c=0):
#     eq = "{}x+{}y+{}=0".format(a,b,c)
#     print(eq)

# lin_eq(2,3)

def slicing(s, start=0, end=-1):
    return s[start: end]  # s[0:-1]=>s[0:5]

s = "python"
print( slicing(s) )
print( slicing(s, 2,3))
print( slicing(s, start=3, end=5))