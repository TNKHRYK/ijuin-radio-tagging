# -*- coding: utf-8 -*-
import sys
import os
# from mutagen.easyid3 import EasyID3
import mutagen


def show_id3_tags(file_path):
    tags = mutagen.id3(file_path)
    print(tags.pprint())

os.chdir('../../music/Radio/伊集院光/深夜の馬鹿力/本放送/深夜の馬鹿力 2018年/')
testfile = 'JUNK伊集院光・深夜の馬鹿力2018年01月01日.mp3'
#tags = mutagen.easyid3(testfile)
#print(tags['title'])

show_id3_tags(testfile)
