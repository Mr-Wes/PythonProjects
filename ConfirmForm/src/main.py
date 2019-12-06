import sys
import os
import pandas as pd
from shutil import copyfile
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
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
        self.setWindowTitle('确认单制作')

    def slotBtSubmit(self):
        # 检测输入
        info = self.getInput()
        print('start test input!')
        if info[0] == '':  # 检测订单号
            QMessageBox.information(self, '提示', '请输入正确订单号！')
        elif info[1] == '':  # 检测客户名称
            QMessageBox.information(self, '提示', '请输入正确客户名！')
        elif info[6] == '':  # 检测型号
            QMessageBox.information(self, '提示', '请选择设备型号！')
        elif info[7] == '':  # 检测数量
            QMessageBox.information(self, '提示', '请输入订单数量!')
        elif info[8] == '':  # 检查主板
            QMessageBox.information(self, '提示', '请选择主板型号！')
        elif info[9] == '':  # 检测显示屏
            QMessageBox.information(self, '提示', '请选择显示屏型号！')
        elif info[14] == '':  # 检测电缆线
            QMessageBox.information(self, '提示', '请选择电缆线型号！')
        else:
            print('end test input!\nstart exec file!')
            # TODO 进度条显示
            # 复制模板
            filename = info[0]+'-'+info[1]+'-'+info[6]+'-'+info[7]+'.xlsx'
            if os.path.exists('../FileDir/' + filename):
                QMessageBox.information(self, '提示', '当前订单确认表已存在！')
            else:
                df = pd.read_excel('../res/001.xlsx')
                print('end exec file!\nstart write data！')
                # 写入数据
                df.iloc[1, 2] = info[0] # 写入订单号
                write = pd.ExcelWriter('../FileDir/'+filename)
                df.to_excel(write, sheet_name='sheet1', index=False)
                write.close()
                print('end write data!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Main()
    mypro = Progress()
    myWin.show()
    sys.exit(app.exec_())
