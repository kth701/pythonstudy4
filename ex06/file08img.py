# 이진파일(이미지, 동영상, 음원,...)

import os
from glob import glob

print('현재 경로:',os.getcwd())
# 1. image 파일 경로
img_path = 'img\\' # 이미지 원본 위치
img_path_copy = os.getcwd() + '/ex06/imgcopy/' # 이미지 이동할 위치

if os.path.exists(img_path):
    # print('원본 이미지 폴더가 존재합니다.')

    # image파일 저장, 이동
    images = []
    # print(img_path_copy)
    # print(os.path.exists(img_path_copy), not( os.path.exists(img_path_copy)) )

    # 이동할 이미지 폴더가 없으면
    if not( os.path.exists(img_path_copy)):
        os.mkdir(img_path_copy)
    else:  # 이동할 이미지 폴더가 있으면
        # image 검색
        # for pic_path in glob(img_path+'apple0[3-4].gif'): # 'img\apple03.gif, apple04.gif' 패턴
        for pic_path in glob(img_path+'*.gif'): # 'img\*.gif' 패턴
            print('원본 이미지 경로:',pic_path)

            # 튜플(경로, 파일이름) 형식으로 분리
            img_path_slice = os.path.split(pic_path)
            # print(img_path_slice, img_path_slice[1]) 

            # 파일이름만 추출
            # images = ['apple01.gif',...]
            images.append(img_path_slice[1])

            try:
                # 이진 파일 읽기
                rfile = open(file=pic_path, mode='rb')
                output = rfile.read() # 파일 전체 읽어와서 output객체 생성

                # 이진 파일 쓰기(생성) : file='이동할 이미지 경로+이미지이름'
                # '/ex06/imgcopy/'+'apple01.gif'
                wfile = open(file=img_path_copy+img_path_slice[1], mode='wb')
                wfile.write(output)

                print('이미지 파일 복사 완료:'+img_path_copy+img_path_slice[1])
            except Exception as e:
                print('Error:',e)
            finally:
                rfile.close()
                wfile.close()
                

            



