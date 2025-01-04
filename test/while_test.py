# while문
# while 조건식:
#     반복 수행구간(참인동안 수행)


# while True:
#     num =  int( input('숫자:'))1
#     if num == 0:
#         continue # 다음 제어문으로 넘어감(조건식 판별)
#         # break # while문을 완전히 빠져나옴
#     print("입력받은 숫자는 ", num)

# for i in range(2,9+1): # 밖같쪽(outer for)
#     print(f"---- {i}단 ---")

#     for j in range(1,9+1): # 안쪽(inner for)
#         print(f"{i} * {j} = {i*j}")

#문장과 단어 추출하기
str = """\
나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 15세입니다.\
"""
print(str)
print(str.split(sep="\n"))

sents = [] #문장을 저장할 리스트 객체
words = [] #단어를 저장할 리스트 객체

# 1. 문단 => 문장
for sen in str.split(sep="\n"): #['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 15세입니다.']
     sents.append(sen)  #문장을 리스트에 추가

     # 문장 -> 단어
     for word in sen.split():
          print(word)
          words.append(word)

print("문장:",sents)
print("문장수:", len(sents)) 

print("단어:", words)
print("단어수:", len(words))
               
