# 텍스트 파일 : 텍스트 자료를 읽어온 자료를 처리하고, 처리 결과를 파일에 저장
# 파일 생성, 파일 읽기 기능
# open(file, mode(r,w,x,a,b), encoding)

# 현재 디렉토리
import os

print(f"현재 경로: {os.getcwd()}")

# 예외 처리
try:
    # 파일 열기
    # ftest1 = open('test01.txt', mode = 'r', encoding='utf-8')
    # ftest1 = open('ex01/sam01.py', mode = 'r', encoding='utf-8')
    ftest1 = open('ex01/sam02.py', mode = 'r', encoding='utf-8')
    # print( ftest1.read())  # 파일 읽기 => 출력

    # 파일 쓰기(저장)
    ftest2 = open ('ex06/data/sam02.py', mode = 'w', encoding='utf-8')
    # ftest2.write('파일 저장하기')
    ftest2.write( ftest1.read() )

    # 파일 쓰기(추가)
    ftest3 = open('ex06/data/appendfile.txt', mode = 'a', encoding='utf-8')
    ftest3.write('Hello Python!!!!\n')

except Exception as e:
    print('Error  발생:',e)
finally:
    # 자원 해제
    ftest1.close()
    ftest2.close()
    ftest2.close()


