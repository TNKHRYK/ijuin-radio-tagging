# coding: utf-8

import os
import time
import mutagen

targetPath = 'test/'

path = os.getcwd()
print(os.getcwd())

srcName = "伊集院光 深夜の馬鹿力 2018年03月19日"

if os.path.exists(targetPath + srcName + '.mp3'):
    os.chdir(targetPath)
    #testfile = open(targetPath + "JUNK伊集院光・深夜の馬鹿力2018年03月19日.mp3")
    #content = testfile.readlines()
    # content = testfile.read()
    time_str = time.strftime('%Y%m%d%H%M%S')
    print(time_str)


    dstName = srcName.replace('伊集院光 深夜の馬鹿力 ','JUNK伊集院光・深夜の馬鹿力')
    os.rename(srcName+'.mp3',dstName+'.mp3')
else:
    print("ないよ")
#os.chdir('/')
#print(os.getcwd())
#print(os.path.relpath(path))
