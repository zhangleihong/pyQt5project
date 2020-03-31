'''

为窗口类添加信号

'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class WinSignal(QWidget):
    # 定义信号对象
    button_clicked_signal = pyqtSignal()
    
    def __init__(self):
        super(WinSignal, self).__init__()
        self.setWindowTitle("标题")
        self.resize(300,100)

        btn = QPushButton('关闭窗口',self)
        # 1.按钮与按钮的槽函数关联
        btn.clicked.connect(self.btn_clicked)
        # 3.信号与信号的槽函数关联
        self.button_clicked_signal.connect(self.btn_close)
        # 2.按钮的槽函数与信号关联关联
    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WinSignal()
    example.show()
    sys.exit(app.exec_())