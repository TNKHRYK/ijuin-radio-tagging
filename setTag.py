#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
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
    #tags['media'] = 'Audio book'
    #tags['date'] = time_str
    #tags['originaldate'] = time_str
    tags.save()
    #print(tags['date'])

def rename(srcFile):
    #time_str = time.strftime('%Y%m%d%H%M%S')
    #print(time_str)
    if '伊集院光 深夜の馬鹿力' in srcFile
        dstName = srcFile.replace('伊集院光 深夜の馬鹿力 ','JUNK伊集院光・深夜の馬鹿力')
    else
        dstName = 'JUNK伊集院光・深夜の馬鹿力xxxx年xx月xx日'
    os.rename(srcFile,dstName)

argvs = sys.argv

if len(argvs) != 2:
    print("MP3ファイルを指定してね")
    sys.exit()

targetFile = argvs[1]
if os.path.exists(targetFile):
    set_id3_tag(targetFile)
    rename(targetFile)
    showId3Tags(targetFile)
else:
    print("対象ファイルが無いよ")
    sys.exit()
