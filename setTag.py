# -*- coding: utf-8 -*-
import sys
import os
from mutagen.easyid3 import EasyID3
import time


def showId3Tags(srcFile):
    tags = EasyID3(srcFile)
    print(tags.pprint())

def set_id3_tag(srcFile):
    tags = EasyID3(srcFile)
    time_str = time.strftime('%Y%m%d%H%M%S')
    tags['author'] = 'ちとん'+time_str
    tags.save()
    print(tags['author'])

def rename(srcFile):
    #testfile = open(targetPath + "JUNK伊集院光・深夜の馬鹿力2018年03月19日.mp3")
    #content = testfile.readlines()
    #content = testfile.read()
    time_str = time.strftime('%Y%m%d%H%M%S')
    #print(time_str)
    dstName = srcFile.replace('26','26')
    os.rename(srcFile,dstName)



targetDir = 'test/'
targetFile = 'JUNK伊集院光・深夜の馬鹿力2018年03月26日.mp3'

os.chdir(targetDir)
if os.path.exists(targetFile):
    showId3Tags(targetFile)
    rename(targetFile)
    set_id3_tag(targetFile)

else:
    print("ファイルが無いよ")
