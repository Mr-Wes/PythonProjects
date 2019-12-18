import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from src.mydesktop_h import Ui_MainWindow


class Mydesktop(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Mydesktop, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('我的桌面')


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    mydesktop = Mydesktop()
    mydesktop.show()
    sys.exit(app.exec_() )