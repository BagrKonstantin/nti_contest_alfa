# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stud_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_name_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_name_2.setGeometry(QtCore.QRect(112, 50, 171, 20))
        self.lineEdit_name_2.setReadOnly(True)
        self.lineEdit_name_2.setObjectName("lineEdit_name_2")
        self.label_35 = QtWidgets.QLabel(self.tab)
        self.label_35.setGeometry(QtCore.QRect(330, 170, 181, 20))
        self.label_35.setObjectName("label_35")
        self.lineEdit_given_by_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_given_by_2.setGeometry(QtCore.QRect(402, 90, 311, 20))
        self.lineEdit_given_by_2.setReadOnly(False)
        self.lineEdit_given_by_2.setObjectName("lineEdit_given_by_2")
        self.pushButton_user = QtWidgets.QPushButton(self.tab)
        self.pushButton_user.setGeometry(QtCore.QRect(20, 350, 61, 23))
        self.pushButton_user.setObjectName("pushButton_user")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(330, 60, 47, 13))
        self.label_44.setObjectName("label_44")
        self.lineEdit_surname_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_surname_2.setGeometry(QtCore.QRect(112, 20, 171, 20))
        self.lineEdit_surname_2.setReadOnly(True)
        self.lineEdit_surname_2.setObjectName("lineEdit_surname_2")
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_41.setObjectName("label_41")
        self.pushButton_first_page = QtWidgets.QPushButton(self.tab)
        self.pushButton_first_page.setGeometry(QtCore.QRect(330, 240, 61, 23))
        self.pushButton_first_page.setObjectName("pushButton_first_page")
        self.lineEdit_birht_date_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_birht_date_2.setGeometry(QtCore.QRect(170, 170, 113, 20))
        self.lineEdit_birht_date_2.setReadOnly(True)
        self.lineEdit_birht_date_2.setObjectName("lineEdit_birht_date_2")
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(330, 90, 71, 16))
        self.label_47.setObjectName("label_47")
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(20, 170, 151, 20))
        self.label_34.setObjectName("label_34")
        self.first_page = QtWidgets.QLabel(self.tab)
        self.first_page.setGeometry(QtCore.QRect(520, 210, 121, 121))
        self.first_page.setObjectName("first_page")
        self.lineEdit_series_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_series_2.setGeometry(QtCore.QRect(402, 30, 101, 20))
        self.lineEdit_series_2.setReadOnly(False)
        self.lineEdit_series_2.setObjectName("lineEdit_series_2")
        self.lineEdit_pass_number_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_pass_number_2.setGeometry(QtCore.QRect(402, 60, 101, 20))
        self.lineEdit_pass_number_2.setReadOnly(False)
        self.lineEdit_pass_number_2.setObjectName("lineEdit_pass_number_2")
        self.lineEdit_sex_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sex_2.setGeometry(QtCore.QRect(110, 110, 171, 20))
        self.lineEdit_sex_2.setReadOnly(True)
        self.lineEdit_sex_2.setObjectName("lineEdit_sex_2")
        self.label_48 = QtWidgets.QLabel(self.tab)
        self.label_48.setGeometry(QtCore.QRect(20, 320, 61, 20))
        self.label_48.setObjectName("label_48")
        self.lineEdit_given_date_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_given_date_2.setGeometry(QtCore.QRect(520, 170, 113, 20))
        self.lineEdit_given_date_2.setReadOnly(False)
        self.lineEdit_given_date_2.setObjectName("lineEdit_given_date_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label.setObjectName("label")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_39.setObjectName("label_39")
        self.user_photo = QtWidgets.QLabel(self.tab)
        self.user_photo.setGeometry(QtCore.QRect(100, 310, 121, 121))
        self.user_photo.setObjectName("user_photo")
        self.lineEdit_code_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_code_2.setGeometry(QtCore.QRect(520, 130, 113, 20))
        self.lineEdit_code_2.setReadOnly(False)
        self.lineEdit_code_2.setObjectName("lineEdit_code_2")
        self.label_46 = QtWidgets.QLabel(self.tab)
        self.label_46.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_46.setObjectName("label_46")
        self.lineEdit_secondname_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_secondname_2.setGeometry(QtCore.QRect(112, 80, 171, 20))
        self.lineEdit_secondname_2.setReadOnly(True)
        self.lineEdit_secondname_2.setObjectName("lineEdit_secondname_2")
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setGeometry(QtCore.QRect(330, 210, 171, 20))
        self.label_42.setObjectName("label_42")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(330, 130, 181, 20))
        self.label_40.setObjectName("label_40")
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(330, 30, 47, 13))
        self.label_45.setObjectName("label_45")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 91, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_phone_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_phone_2.setGeometry(QtCore.QRect(130, 100, 151, 20))
        self.lineEdit_phone_2.setReadOnly(False)
        self.lineEdit_phone_2.setObjectName("lineEdit_phone_2")
        self.label_49 = QtWidgets.QLabel(self.tab_2)
        self.label_49.setGeometry(QtCore.QRect(38, 170, 31, 16))
        self.label_49.setObjectName("label_49")
        self.lineEdit_email_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_email_2.setGeometry(QtCore.QRect(112, 30, 171, 20))
        self.lineEdit_email_2.setReadOnly(True)
        self.lineEdit_email_2.setObjectName("lineEdit_email_2")
        self.lineEdit_adress_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_adress_2.setGeometry(QtCore.QRect(90, 170, 331, 20))
        self.lineEdit_adress_2.setReadOnly(False)
        self.lineEdit_adress_2.setObjectName("lineEdit_adress_2")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_37.setObjectName("label_37")
        self.label_43 = QtWidgets.QLabel(self.tab_2)
        self.label_43.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_43.setObjectName("label_43")
        self.label_50 = QtWidgets.QLabel(self.tab_2)
        self.label_50.setGeometry(QtCore.QRect(40, 210, 101, 16))
        self.label_50.setObjectName("label_50")
        self.lineEdit_adress_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_adress_3.setGeometry(QtCore.QRect(140, 210, 271, 20))
        self.lineEdit_adress_3.setReadOnly(False)
        self.lineEdit_adress_3.setObjectName("lineEdit_adress_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_52 = QtWidgets.QLabel(self.tab_3)
        self.label_52.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_52.setObjectName("label_52")
        self.lineEdit_number_of_doc_frame_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_number_of_doc_frame_3.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit_number_of_doc_frame_3.setReadOnly(True)
        self.lineEdit_number_of_doc_frame_3.setObjectName("lineEdit_number_of_doc_frame_3")
        self.lineEdit_direction = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_direction.setGeometry(QtCore.QRect(120, 110, 113, 22))
        self.lineEdit_direction.setReadOnly(True)
        self.lineEdit_direction.setObjectName("lineEdit_direction")
        self.label_59 = QtWidgets.QLabel(self.tab_3)
        self.label_59.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_59.setObjectName("label_59")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_direction_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_direction_2.setGeometry(QtCore.QRect(120, 10, 113, 22))
        self.lineEdit_direction_2.setReadOnly(True)
        self.lineEdit_direction_2.setObjectName("lineEdit_direction_2")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 171, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 171, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 101, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(654, 530, 111, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_35.setText(_translate("MainWindow", "Дата выдачи (мм-дд-гггг)"))
        self.pushButton_user.setText(_translate("MainWindow", "просмотр"))
        self.label_44.setText(_translate("MainWindow", "Номер"))
        self.label_41.setText(_translate("MainWindow", "Отчество"))
        self.pushButton_first_page.setText(_translate("MainWindow", "просмотр"))
        self.label_47.setText(_translate("MainWindow", "кем выдан"))
        self.label_34.setText(_translate("MainWindow", "Дата рождения (мм-дд-гггг)"))
        self.first_page.setText(_translate("MainWindow", "Фото"))
        self.label_48.setText(_translate("MainWindow", "Фото"))
        self.label.setText(_translate("MainWindow", "пол"))
        self.label_39.setText(_translate("MainWindow", "Фамилия"))
        self.user_photo.setText(_translate("MainWindow", "Фото"))
        self.label_46.setText(_translate("MainWindow", "Имя"))
        self.label_42.setText(_translate("MainWindow", "фотоскан первой страницы"))
        self.label_40.setText(_translate("MainWindow", "код подразделения (***-***)"))
        self.label_45.setText(_translate("MainWindow", "Серия"))
        self.label_2.setText(_translate("MainWindow", "год поступления"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Основное"))
        self.label_49.setText(_translate("MainWindow", "Адрес по прописке"))
        self.label_37.setText(_translate("MainWindow", "email"))
        self.label_43.setText(_translate("MainWindow", "Номер телофона"))
        self.label_50.setText(_translate("MainWindow", "Адрес проживания"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Контакты"))
        self.label_52.setText(_translate("MainWindow", "Направление"))
        self.label_59.setText(_translate("MainWindow", "Номер документа"))
        self.label_3.setText(_translate("MainWindow", "Факультет"))
        self.label_4.setText(_translate("MainWindow", "Номер группы"))
        self.label_5.setText(_translate("MainWindow", "Номер студенческого\n"
"билета и зачетной книжки"))
        self.label_6.setText(_translate("MainWindow", " Номер читательского билета"))
        self.label_7.setText(_translate("MainWindow", "Дата зачисления"))
        self.label_8.setText(_translate("MainWindow", "Дата отчисления"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Обучение"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить и выйти"))
