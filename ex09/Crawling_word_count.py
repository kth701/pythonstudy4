
# 웹 크롤링해서 수집한 자료 단어 출현빈도수 시각화
#  pickle.load()-> text  처리 -> word count
import pickle
import re
from collections import Counter

# 1. 크롤링해서 수집한 이진 파일 호출
file = open('data.pickle', mode="rb")
news_data2 = pickle.load(file)
# print(news_data2) # 텍스트 -> 리스트 구조

# 2. text 전ㅊ리
def clean_text(text_string):
    # 2.1 문장 부호 제거 : 따옴표 추가 (\'\")
    # print("2.1 text 문장부호 제거:")
    # 정규식 패턴으로 문장 부호 제거 처리
    text_string_re = re.sub('[,.?!:\'\"\]\[;]','', text_string)
    # print(text_string_re)

    # 2.2 특수문자, 숫자 제거
    # print("2.2 특수문자, 숫자 제거:")
    text_string_re = re.sub('[!@#$%^&*()|[0-9]','', text_string_re)
    # print(text_string_re)

    # 2.3 영문 소문자-> 영문 제거 
    # print("2.3 특수문자, 숫자 제거:") 
    # text_string_re = text_string_re.lower()
    text_string_re = re.sub('[a-z]','',text_string_re)
    # print(text_string_re) 
    

    # 2.4 공백 제거
    # print("2.4 공백 제거:") 
    text_string_re = ' '.join(text_string_re.split()) #'홍길동 김길순'
    # print(text_string_re)

    # print("-"*30)

    return text_string_re
    

# 3. 텍스트 처리하는 함수 호출
# clean_texts = clean_text("abcd',.[]]\"")
print("-"*30)
clean_texts = [clean_text(row) for row in news_data2]
# print("text처리후 결과:")
# print(clean_texts)

# 4. 단어 빈도수
word_count = {}
for text in clean_texts:
    # print(text)
    for word in text.split(): # 문장 -> 단어 (공백기준으로 분리)
        # print(word)
        word_count[word] = word_count.get(word, 0)+1


print(">> word count <<")        
# print(word_count)
# for w in word_count:
#     print(w)

# 불용 단어 제거
# del word_count['[바로잡습니다]']

# 3회 이상 출현 단어이고, 2-4자 단어 선정
new_word_count = {}
for word, cnt in  word_count.items(): # word_count.keys(), word_count.values()
    # print(word(key), cnt(value))
    # cnt:빈도수 2회이상, 단어길이 2~4사이인 단어만 처리
    if cnt >=2 and len(word) >=2 and len(word) <=4 :
        print(word, '->', word_count[word])
        new_word_count[word] = new_word_count.get(word, cnt)

print("-"*30)
print(new_word_count)
print("-"*30)

# Top word Counter
counter = Counter(new_word_count) # 생성자 -> object
top5 = counter.most_common(5) # 상위 5개 리스트 구조형식으로 반환
print(top5)

words = [] #단어
counts = [] #출현빈도수
for word, count in top5:
    words.append(word)
    counts.append(count)
print("="*30)
print(words) # 출현 단어
print(counts) # 출현 단어 빈도수


# 데이터 시각화 
import matplotlib.pyplot as plt

# 차트에서 한글 font 지원
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf').get_name()
rc('font', family=font_name)


# 선 그래프
print('선 그래프')
plt.plot(words, counts) # xxx.plot(x축:단어, y축:단어 빈도수)
plt.show() # 차트를 화면에 표시

print('막대 그래프')
plt.bar(words, counts)
plt.show()
