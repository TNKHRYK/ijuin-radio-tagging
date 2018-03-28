# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
import mutagen

class DropWidget(QWidget):

    def __init__(self, parent=None):
        super(DropWidget, self).__init__(parent)
        self.statusLabel = QLabel('ここにMP3ファイルをドラッグ＆ドロップ', self)
        self.statusLabel.resize(600,300)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()
        '''
        mimeData = event.mimeData()
        print('dragEnterEvent')
        for mimetype in mimeData.formats():
            print('MIMEType:', mimetype)
            print('Data:', mimeData.data(mimetype))
            print()
        #print()
        '''


    def dropEvent(self, event):
        event.accept()
        mimeData = event.mimeData()
        print('dropEvent')
        l = "ファイル読み込み<br>"
        for mimetype in mimeData.formats():
            #print('MIMEType:', mimetype)
            l+='MIMEType:' + mimetype + '<br>'
            # print('Data:', mimeData.data(mimetype))
            l+='Data:' + str(mimeData.data(mimetype)) + '<br>'
        self.statusLabel.setText(l)
        print(l)

        print()
        print(os.path.exists('/usr/hoge/'))
        testfile = open("test.txt")
        path = '/user/Dropbox/music/Radio/伊集院光/深夜の馬鹿力/本放送/深夜の馬鹿力 2018年/JUNK伊集院光・深夜の馬鹿力2018年01月01日.mp3'
        #path = str(mimeData.data(mimetype))
        tags = mutagen.easyEasyID3(path)
        #print(tags)

def main():
    app = QApplication(sys.argv)
    w = DropWidget()
    #label = QLabel('ここにMP3ファイルをドラッグ＆ドロップ', w)
    w.setWindowTitle("恥豚MP3タグ付け君")
    w.resize(600, 600)
    w.show()
    w.raise_()
    app.exec_()

if __name__ == '__main__':
    main()
