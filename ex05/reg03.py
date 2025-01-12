from re import split, match, compile

# 더미 텍스트 자료
multi_line ="""\
http://www.naver.com
http://www.daum.net
www.hongkildong.com\
"""
print( multi_line)

# 구분자를 이용 하여 문자열 분리
web_site = split("\n", multi_line)
print( web_site)

# 패턴 객체 만들기
pat = compile("http://")

sel_site = [ site for site in web_site if match(pat, site)]
print(sel_site)

