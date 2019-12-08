import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from src import util
from src.confirm import Ui_Fconfirm
from src.progress import Ui_Dprogress


class Progress(QWidget, Ui_Dprogress):
    def __init__(self, parent=None):
        super(Progress, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('进度')


class Main(QWidget, Ui_Fconfirm):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        # 向界面传送选择框数据
        self.setChoiceData(util.readXML('../res/choice.xml'))
        self.setWindowTitle('确认单制作')

    def slotBtSubmit(self):
        # 检测输入
        info = self.getInput()
        print('start test input!')
        if util.testInput(self, info):
            print('end test input!\nstart exec file!')
            # TODO 进度条显示
            # 生成文件
            filepath = '../FileDir/' + info[0] + '-' + info[1] + '-' + info[6] + '-' + info[7] + '.xlsx'
            if util.createFile(self, '../res/001.xlsx', filepath):
                print('end exec file!\nstart write data！')
                # 写入数据
                if util.writeFile(self, info, filepath):
                    print('end write data!')
                    self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Main()
    mypro = Progress()
    myWin.show()
    sys.exit(app.exec_())
