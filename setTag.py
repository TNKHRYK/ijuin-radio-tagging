#! /usr/bin/env python3
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
    time_str = time.strftime('%Y%m%d')
    tags['author'] = '伊集院 光'
    tags['artist'] = '伊集院 光'
    tags['album'] = '深夜の馬鹿力 '+ time.strftime('%Y') +'年'
    tags['genre'] = 'Radio'
    tags['date'] = time_str
    tags.save()
    print(tags['date'])

def rename(srcFile):
    #time_str = time.strftime('%Y%m%d%H%M%S')
    #print(time_str)
    dstName = srcFile.replace('伊集院光 深夜の馬鹿力 ','JUNK伊集院光・深夜の馬鹿力')
    dstName = dstName + '.mp3'
    os.rename(srcFile,dstName)

targetDir = 'test/'
targetFile = 'ちとんテスト.mp3' #'JUNK伊集院光・深夜の馬鹿力2018年03月26日.mp3'

os.chdir(targetDir)
if os.path.exists(targetFile):
    showId3Tags(targetFile)
    set_id3_tag(targetFile)
    rename(targetFile)
else:
    print("ファイルが無いよ")
