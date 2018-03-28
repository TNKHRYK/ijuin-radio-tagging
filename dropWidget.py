# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets
import PyQt5.QtCore
#from PyQt5.QtWidgets import QApplication, QWidget


print(PyQt5.QtCore.QT_VERSION_STR)

if __name__ == '__main__':

    app = PyQt5.QtWidgets.QApplication(sys.argv)

  #  w = QWidget.QLabel("test")
    w = PyQt5.QtWidgets.QLabel("Hello worldにはねーーーーー")
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')

    w.show()

    sys.exit(app.exec_())


#a = PyQt5.QtWidgets.QApplication(sys.argv)
#w = PyQt5.QtWidgets.QLabel("Hello world")
#w.show()
#exit(a.exec_())
