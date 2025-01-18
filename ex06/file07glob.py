# glob모듈: 유닉스 쉘이 사용한 규칙에 의해서 지정된 패턴과 일하는
#         : 모든 파일과 디렉터리의 목록을 반환
#         : 특수문자(*.?,[])

import glob
import os.path

print("- ", os.getcwd())
os.chdir('ex04')
print("- ", os.getcwd())

print(glob.glob('*.txt'))
print(glob.glob('fun0[1-3].py')) # fun01, fun02, fun03