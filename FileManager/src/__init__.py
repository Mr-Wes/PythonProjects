import json
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from os import path, listdir
from src.Main import Ui_Form
from src.utils import formatFileName, initFile

file_name = '/.file_manager.json'


class Main(QWidget, Ui_Form):
    basedir = None
    list0 = []  # 用于存储当前路径下的文件夹
    list1 = []  # 用于存储当前路径下的文件
    FLAG_JSON = False  # 当前文件夹下是否有json文件
    FLAG_EDITABLE = False  # 输入框是否可编辑
    file = None  # json文件
    json_date = None  # 从文件读取到的数据
    selectName = None  # 当前列表中选中的文件名

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('文件管理系统v1.0')
        self.pages.hide()
        # 为控件指定信号与槽
        self.le_path.returnPressed.connect(self.queryFunction)
        self.lv_file.clicked.connect(self.ItemClick)
        self.lv_file.doubleClicked.connect(self.ItemDoubleClick)
        self.bt.clicked.connect(self.buttonClick)
        # 获取程序所在目录
        self.basedir = path.dirname(sys.argv[0])
        self.basedir = self.basedir.replace('\\\\', '/')
        self.basedir = self.basedir.replace('\\', '/')
        # 进入目录
        self.inNewDir()
        # 将当前目录写到LineEdit中
        self.writePath(self.basedir)
        # 历遍当前目录下所有文件，并在list中显示
        self.toListDate(self.basedir)

    # 根据指定路径，获得路径下所有文件，并写入到list0，和list1中，并将数据推送到ListView
    def toListDate(self, basedir):
        lists = listdir(basedir)  # 获得当前目录下所有文件名
        self.list0 = []  # 清空数据
        self.list1 = []  # 清空数据
        date = ['  文件（夹）名称', '   ...   ']
        for i in lists:
            if path.isdir(path.join(basedir, i)):  # 是文件夹
                self.list0.insert(0, i)
                date.insert(2, '  📁  ' + formatFileName(i))
            else:  # 是文件
                self.list1.append(i)
                date.append('  📦  ' + formatFileName(i))
        self.writeList(date)

    # index-【0：1】：标题，【2：1+len(list0)】：文件夹，【2+len(list0)：1+len(list0)+len(list1)】：文件
    # 列表条目的单击事件
    def ItemClick(self, item):
        index = item.row()
        if index < 2:
            self.selectName = None
            self.pages.hide()
        else:
            self.pages.show()
            lists = self.list0 + self.list1
            self.selectName = lists[index - 2]
            if self.FLAG_JSON:  # 有json文件
                # 根据json查找数据
                if self.selectName in self.json_date:
                    self.writeDetail(self.json_date[self.selectName])
                else:
                    self.hintDetail()
            else:  # 没有json文件
                self.hintDetail()

    # 列表条目的双击事件
    def ItemDoubleClick(self, item):
        index = item.row()
        # 判断是否是文件夹
        if 1 < index < 2 + len(self.list0):  # 文件夹
            if self.basedir[-1] == '/':
                self.leaveToNewDir(self.basedir + self.list0[index - 2])
            else:
                self.leaveToNewDir(self.basedir + '/' + self.list0[index - 2])
        elif index > 1 + len(self.list0):  # 文件
            self.ItemClick(item)
        elif index == 1:  # ...
            a = self.basedir.split('/')
            if len(a) > 2:
                l = len(a[-1])  # 最后一个文件夹名称字符数
                self.leaveToNewDir(self.basedir[0:-1 - l])
            elif len(a) == 2 and a[1] != '':  # D:/XXX
                self.leaveToNewDir(a[0] + '/')

    # 编辑/保存按钮的点击事件
    def buttonClick(self):
        if self.te_detail.isReadOnly():  # 开始编辑
            self.bt.setStyleSheet("border-image: url(:/frameon.png);")
            self.te_detail.setReadOnly(False)
            if self.te_detail.toPlainText() == '最多可输入250个字符':
                self.te_detail.setText('')
        else:  # 开始保存
            self.te_detail.setReadOnly(True)
            if self.te_detail.toPlainText() != '':
                if self.FLAG_JSON is False:
                    initFile(self.basedir + file_name)
                    self.FLAG_JSON = True
                    self.file = open(self.basedir + file_name, 'r+', encoding='utf-8')
                    self.json_date = json.load(self.file)
                self.json_date[self.selectName] = self.te_detail.toPlainText()
            else:
                self.hintDetail()
            self.bt.setStyleSheet("border-image: url(:/frameoff.png);")

    # 输入框按回车触发函数
    def queryFunction(self):
        input_path = self.le_path.displayText()
        if len(input_path.split('\\')) > 1:
            QMessageBox.warning(self, '警告！', '本程序只支持“/”作为路径分隔符，请重新输入！')
        else:
            if input_path[-1] == ':':  # 输入的是盘符
                input_path = input_path + '/'
                if path.isdir(input_path):
                    self.leaveToNewDir(input_path)
                else:
                    QMessageBox.warning(self, '错误！', '您输入的不是合法路径，请您重新输入！')
            elif path.isdir(input_path):  # 输入的是文件夹路径
                if input_path[-1] == '/' and len(input_path.split('/')) > 2:
                    input_path = input_path[0:-1]
                self.leaveToNewDir(input_path)
            elif path.isfile(input_path):  # 输入的是文件路径
                l = len(path.basename(input_path))  # 文件名长度，即为截取字符数
                l = l if len(input_path.split('/')) == 2 else l + 1  # 除非遇 D:/XXX.XXX 否则多截一个“/”
                self.leaveToNewDir(input_path[0:0 - l])
                # TODO 同时自动选择该文件
            else:
                QMessageBox.warning(self, '错误！', '您输入的不是合法路径，请您重新输入！')

    # 进入目录时检测是否有json文件, 初始化FLAG—_JSON，file，json_date
    def inNewDir(self):
        if path.exists(self.basedir + file_name):
            self.FLAG_JSON = True
            self.file = open(self.basedir + file_name, 'r+', encoding='utf-8')
            self.json_date = json.load(self.file)
        else:
            self.FLAG_JSON = False

    # 离开当前文件夹时，要写入数据，关闭文件，清空缓存
    def leaveToNewDir(self, new_dir):
        self.pages.hide()
        self.selectName = None
        if self.FLAG_JSON:
            # 删除无用文件
            r = {'文件名称': '备注内容'}
            for key in self.json_date:
                if key in self.list0 + self.list1:
                    r[key] = self.json_date[key]
            self.json_date = r
            self.file.seek(0)
            self.file.truncate()
            self.file.write(json.dumps(self.json_date))
            self.file.close()
            self.json_date = None
        self.basedir = new_dir
        self.inNewDir()
        self.writePath(new_dir)
        self.toListDate(new_dir)

    def writePath(self, path):
        self.le_path.setText(path)

    def writeList(self, lists):
        slm = QStringListModel()
        slm.setStringList(lists)
        self.lv_file.setModel(slm)

    def hintDetail(self):
        _translate = QtCore.QCoreApplication.translate
        self.te_detail.setHtml(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f8f8f;\">最多可输入250个字符</span></p></body></html>"))

    def writeDetail(self, str):
        _translate = QtCore.QCoreApplication.translate
        self.te_detail.setHtml(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">" + str + "</span></p></body></html>"))

    def closeEvent(self, QCloseEvent):
        if self.FLAG_JSON:
            # 删除无用文件
            r = {'文件名称':'备注内容'}
            for key in self.json_date:
                if key in self.list0 + self.list1:
                    r[key] = self.json_date[key]
            self.json_date = r
            self.file.seek(0)
            self.file.truncate()
            self.file.write(json.dumps(self.json_date))
            self.file.close()
        QCloseEvent.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
