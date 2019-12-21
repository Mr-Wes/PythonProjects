import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from src.Main import Ui_MainWindow
from src.handleXML import writeRep, getRepsName, createXML


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("W's File")
        # 获取配置文件中所有仓库名
        names = getRepsName()
        # TODO 将 names 刷新 lv_reps

    def slotSelectDir(self):
        # 选择作为仓库的文件夹
        dir = QFileDialog.getExistingDirectory()
        dirname = os.path.basename(dir)
        # 将文件夹路径及名称写入到配置文件
        writeRep(dirname, dir)
        # TODO 创建相应的 xml 文件
        createXML(dirname, 'files')
        # TODO 将文件夹名称传入 lv_reps,并刷新


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Main()
    myWin.show()
    sys.exit(app.exec_())