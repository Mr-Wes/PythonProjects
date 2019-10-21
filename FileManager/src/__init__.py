import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.Main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("W's File")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Main()
    myWin.show()
    sys.exit(app.exec_())