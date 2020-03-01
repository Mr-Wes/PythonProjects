import sys

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow,QApplication

from src.mydesktop_h import Ui_MainWindow


class Mydesktop(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Mydesktop, self).__init__(parent)
        self.setupUi(self)
        self.showFullScreen()
        self.setWindowTitle('我的桌面')
        # TODO 获取设备屏幕分辨率与尺寸，以定制左侧网格窗口的横纵列数
        # TODO 调整左侧网格窗口

    def timer(self):
        pass

    def enterEvent(self, *args, **kwargs):
        pass

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    mydesktop = Mydesktop()
    mydesktop.show()
    sys.exit(app.exec_())