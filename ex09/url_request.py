# 원격 서버에서 자료 수집하기

# requst, BeautifulScoup모듈을 import
import urllib.request           # 원격 서버 파일 요청
from bs4 import BeautifulSoup   # html파싱

# 요청할 url
url = 'http://www.naver.com/index.html'

# 원격 서버 파일 요청
resp = urllib.request.urlopen(url)
data = resp.read() # 서버로 부터 응답받은 객체를 파일 형식으로 읽기

# 문자 디코딩
src = data.decode("utf-8") 
print('source')
print(src)
print("-"*30)

# html source 파싱
html = BeautifulSoup(src, 'html.parser')
print('html 파싱')
print(html)

print("-"*30)
# index.html 태그중 특정 태그 내용
a = html.find('a')
print('a 태그:', a)
print('a 태그 내용:',a.string)





