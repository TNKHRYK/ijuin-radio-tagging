# -*- coding: utf-8 -*-
import sys
import os
from mutagen.easyid3 import EasyID3
import time


def show_id3_tags(file_path):
    tags = EasyID3(file_path)
    print(tags.pprint())

def rename(srcName):
    #testfile = open(targetPath + "JUNK伊集院光・深夜の馬鹿力2018年03月19日.mp3")
    #content = testfile.readlines()
    #content = testfile.read()
    time_str = time.strftime('%Y%m%d%H%M%S')
    print(time_str)
    dstName = srcName.replace('26',time_str)
    os.rename(srcName,dstName)


targetDir = 'test/'
targetFile = 'JUNK伊集院光・深夜の馬鹿力2018年03月26日.mp3'

os.chdir(targetDir)
if os.path.exists(targetFile):
    show_id3_tags(targetFile)
    rename(targetFile)
else:
    print("ファイルが無いよ")
