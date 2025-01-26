
import matplotlib.pyplot as plt # 차트 생성
import random # 차트 자료 생성
import matplotlib # 음수 부호 지원=> 음수 부호가 깨지지 않도록 음수 부호를 지원
matplotlib.rcParamsDefault['axes.unicode_minus'] = False

for i in range(5):
    # print(random.randint(a=1, b=5), end=" ") # 1~5  
    # print(random.random()) # 0 < n < 1
    # 표준 정규분포: 평균과 표준편차를 인수로 하여 정규분포를 따르는 난수
    print(random.normalvariate(mu=0, sigma=1)) 

print("-"*20)

# 1. 기본 차트
data = range(10)
# 1개의 인자만 적용 : plot(y), x:자료의 색인으로 차트를 그려줌
# 2개 인자: x:data1, y: data2

# plt.plot(data) 
# plt.show()

# 3개 인자: x, y, z(카커 효과 추가)
# plt.plot(data, 'r+')
# plt.show()


# 2개 data
data2 = [random.random() for i in range(10)]
# plt.plot(data, data2) # line
# plt.plot(data, data2, 'ro') # point추가
# plt.show()

# 산점도 그리기

# 단색
# plt.scatter(x=data, y=data2, c='b', marker='o')
# plt.show()

# 여러가지 색
# print('여러가지 색 산점도')
# cdata = [random.randint(a=1, b=3) for i in range(10)]
# plt.scatter(x=data, y=data2, c=cdata, marker='o')
# plt.show()

# 히스토그램 
print('히스토그램')
# 정규 분포
# data3 = [random.normalvariate(mu=0, sigma=1) for i in range(1000)]
# plt.hist(data3)
# plt.show()

# 균등 분포
# data4 = [random.uniform(a=1, b=100) for i in range(1000)]
# plt.hist(data4)
# plt.show()

#  차트 크기 지정
fig = plt.figure(figsize=(12,5)) # (w, h)
chart = fig.add_subplot(1,1,1)

# data4 = [random.random() for i in range(50)]
# chart.plot(data4, color='r', label='step', drawstyle='steps-post')
# plt.show()


data5 = [random.random() for i in range(50)]
chart.plot(data5, color='b', label='line')
# plt.show()



# 차트 구성 요소 추가
plt.title("step and laine graph") # 제목
plt.xlabel("index") # 축 이름
plt.ylabel("random number") # y축 이름
plt.legend(loc='best') # 범례

plt.show()