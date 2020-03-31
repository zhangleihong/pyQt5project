"""
@project:pyQt5project
@author:zlh
@file:WebEngineView.py
@time:2020/3/30 21:20
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class WebEngineView(QMainWindow):

    def __init__(self ):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.jd.com'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = WebEngineView()
	win.show()
	sys.exit(app.exec_())

#python -m PyQt5.uic.pyuic untitled.ui -o untitled.py