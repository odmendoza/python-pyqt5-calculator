# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/odmendoza/Repositories/python-pyqt5-calculator/src/ui/calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 247)
        self.lineEdit_in_out = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_in_out.setGeometry(QtCore.QRect(20, 10, 251, 51))
        self.lineEdit_in_out.setObjectName("lineEdit_in_out")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 70, 254, 170))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 3, 0, 1, 1)
        self.pushButton_substract = QtWidgets.QPushButton(self.widget)
        self.pushButton_substract.setObjectName("pushButton_substract")
        self.gridLayout.addWidget(self.pushButton_substract, 3, 1, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.widget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 2, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.widget)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 4, 0, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.widget)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 4, 1, 1, 1)
        self.pushButton_equal = QtWidgets.QPushButton(self.widget)
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout.addWidget(self.pushButton_equal, 4, 2, 1, 1)
        self.pushButton_ac = QtWidgets.QPushButton(self.widget)
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.gridLayout.addWidget(self.pushButton_ac, 5, 1, 1, 1)
        self.pushButton_info = QtWidgets.QPushButton(self.widget)
        self.pushButton_info.setObjectName("pushButton_info")
        self.gridLayout.addWidget(self.pushButton_info, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_add.setText(_translate("Dialog", "+"))
        self.pushButton_substract.setText(_translate("Dialog", "-"))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_multiply.setText(_translate("Dialog", "*"))
        self.pushButton_divide.setText(_translate("Dialog", "/"))
        self.pushButton_equal.setText(_translate("Dialog", "="))
        self.pushButton_ac.setText(_translate("Dialog", "AC"))
        self.pushButton_info.setText(_translate("Dialog", "Info"))
