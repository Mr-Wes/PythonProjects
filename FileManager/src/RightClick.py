# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RightClick.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(120, 150)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 121, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_open = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_open.setObjectName("lb_open")
        self.verticalLayout.addWidget(self.lb_open)
        self.lb_openWays = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_openWays.setObjectName("lb_openWays")
        self.verticalLayout.addWidget(self.lb_openWays)
        self.lb_openFile = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_openFile.setObjectName("lb_openFile")
        self.verticalLayout.addWidget(self.lb_openFile)
        self.lb_cut = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_cut.setObjectName("lb_cut")
        self.verticalLayout.addWidget(self.lb_cut)
        self.lb_copy = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_copy.setObjectName("lb_copy")
        self.verticalLayout.addWidget(self.lb_copy)
        self.lb_delete = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_delete.setObjectName("lb_delete")
        self.verticalLayout.addWidget(self.lb_delete)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_open.setText(_translate("Form", "  打开"))
        self.lb_openWays.setText(_translate("Form", "  打开方式"))
        self.lb_openFile.setText(_translate("Form", "  打开所在文件夹"))
        self.lb_cut.setText(_translate("Form", "  剪切"))
        self.lb_copy.setText(_translate("Form", "  复制"))
        self.lb_delete.setText(_translate("Form", "  删除"))
