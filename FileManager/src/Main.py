# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from src import image_rc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("QWidget#widget{\n"
"    border-image: url(:/background.jpg);\n"
"}\n"
"QListView#lv_file{\n"
"    border-image: url(:/flock.jpg);\n"
"}\n"
"QLabel#lb_null{\n"
"    border-image: url(:/tree.jpg);\n"
"}\n"
"QTextEdit#te_detail{\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"QPushButton#bt{\n"
"    border-image: url(:/frameoff.png)\n"
"}\n"
"QLineEdit#le_path{\n"
"    border:1px solid gray\n"
"    border-radius:10px\n"
"}")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(10, 6, 10, 6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_1 = QtWidgets.QWidget(self.widget)
        self.widget_1.setObjectName("widget_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.le_path = QtWidgets.QLineEdit(self.widget_1)
        self.le_path.setObjectName("le_path")
        self.verticalLayout.addWidget(self.le_path)
        self.lv_file = QtWidgets.QListView(self.widget_1)
        self.lv_file.setObjectName("lv_file")
        self.verticalLayout.addWidget(self.lv_file)
        self.horizontalLayout.addWidget(self.widget_1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.page_null = QtWidgets.QWidget(self.widget_2)
        self.page_null.setGeometry(QtCore.QRect(0, 0, 330, 578))
        self.page_null.setObjectName("page_null")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_null)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_null = QtWidgets.QLabel(self.page_null)
        self.lb_null.setText("")
        self.lb_null.setObjectName("lb_null")
        self.verticalLayout_2.addWidget(self.lb_null)
        self.pages = QtWidgets.QWidget(self.widget_2)
        self.pages.setGeometry(QtCore.QRect(0, 0, 330, 578))
        self.pages.setObjectName("pages")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pages)
        self.verticalLayout_3.setContentsMargins(12, 0, 20, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.pages)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bt = QtWidgets.QPushButton(self.pages)
        self.bt.setMinimumSize(QtCore.QSize(50, 26))
        self.bt.setObjectName("bt")
        self.horizontalLayout_3.addWidget(self.bt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.te_detail = QtWidgets.QTextEdit(self.pages)
        self.te_detail.setObjectName("te_detail")
        self.verticalLayout_3.addWidget(self.te_detail)
        self.preview = QtWidgets.QWidget(self.pages)
        self.preview.setObjectName("preview")
        self.verticalLayout_3.addWidget(self.preview)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 20)
        self.verticalLayout_3.setStretch(3, 20)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\"> 路径</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\"> 文件备注</span></p></body></html>"))
        self.te_detail.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f8f8f;\">最多可输入250个字符</span></p></body></html>"))
