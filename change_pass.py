# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_pass.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 239)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label.setObjectName("label")
        self.lineEdit_login = QtWidgets.QLineEdit(Form)
        self.lineEdit_login.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_old_pass = QtWidgets.QLineEdit(Form)
        self.lineEdit_old_pass.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.lineEdit_old_pass.setObjectName("lineEdit_old_pass")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 91, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_new_pass = QtWidgets.QLineEdit(Form)
        self.lineEdit_new_pass.setGeometry(QtCore.QRect(160, 110, 113, 22))
        self.lineEdit_new_pass.setObjectName("lineEdit_new_pass")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_submit_pass = QtWidgets.QLineEdit(Form)
        self.lineEdit_submit_pass.setGeometry(QtCore.QRect(160, 150, 113, 22))
        self.lineEdit_submit_pass.setObjectName("lineEdit_submit_pass")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Логин"))
        self.label_2.setText(_translate("Form", "Старый пароль"))
        self.label_3.setText(_translate("Form", "Новый пароль"))
        self.label_4.setText(_translate("Form", "Подтвердите пароль"))
        self.pushButton.setText(_translate("Form", "Подтвердить"))
