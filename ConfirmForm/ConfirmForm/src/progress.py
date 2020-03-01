# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dprogress(object):
    def setupUi(self, Dprogress):
        Dprogress.setObjectName("Dprogress")
        Dprogress.resize(400, 80)
        Dprogress.setMinimumSize(QtCore.QSize(400, 80))
        Dprogress.setMaximumSize(QtCore.QSize(400, 80))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dprogress)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dprogress)
        self.label.setText("hi")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(Dprogress)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dprogress)
        QtCore.QMetaObject.connectSlotsByName(Dprogress)

    def retranslateUi(self, Dprogress):
        _translate = QtCore.QCoreApplication.translate
        Dprogress.setWindowTitle(_translate("Dprogress", "Dialog"))

    def setLabelValue(self, value):
        self.label.setText(value)

    def setProgressValue(self, value):
        self.progressBar.setValue(value)