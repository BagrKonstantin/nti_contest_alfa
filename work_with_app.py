# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_with_app.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1005, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 941, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_greeting = QtWidgets.QFrame(self.tab)
        self.frame_greeting.setGeometry(QtCore.QRect(0, 10, 851, 631))
        self.frame_greeting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_greeting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_greeting.setObjectName("frame_greeting")
        self.label_29 = QtWidgets.QLabel(self.frame_greeting)
        self.label_29.setGeometry(QtCore.QRect(30, 0, 671, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.pushButton_change_pass = QtWidgets.QPushButton(self.frame_greeting)
        self.pushButton_change_pass.setGeometry(QtCore.QRect(20, 70, 121, 28))
        self.pushButton_change_pass.setObjectName("pushButton_change_pass")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_greeting)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 811, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label_30 = QtWidgets.QLabel(self.frame_greeting)
        self.label_30.setGeometry(QtCore.QRect(180, 80, 71, 16))
        self.label_30.setObjectName("label_30")
        self.lineEdit_fakultet_stud = QtWidgets.QLineEdit(self.frame_greeting)
        self.lineEdit_fakultet_stud.setGeometry(QtCore.QRect(260, 80, 113, 22))
        self.lineEdit_fakultet_stud.setReadOnly(True)
        self.lineEdit_fakultet_stud.setObjectName("lineEdit_fakultet_stud")
        self.label_32 = QtWidgets.QLabel(self.frame_greeting)
        self.label_32.setGeometry(QtCore.QRect(390, 80, 81, 16))
        self.label_32.setObjectName("label_32")
        self.lineEdit_napravlenie_stud = QtWidgets.QLineEdit(self.frame_greeting)
        self.lineEdit_napravlenie_stud.setGeometry(QtCore.QRect(480, 80, 113, 22))
        self.lineEdit_napravlenie_stud.setReadOnly(True)
        self.lineEdit_napravlenie_stud.setObjectName("lineEdit_napravlenie_stud")
        self.pushButton_raspisanie = QtWidgets.QPushButton(self.frame_greeting)
        self.pushButton_raspisanie.setGeometry(QtCore.QRect(740, 80, 93, 28))
        self.pushButton_raspisanie.setObjectName("pushButton_raspisanie")
        self.pushButton_dek_and_rek = QtWidgets.QPushButton(self.frame_greeting)
        self.pushButton_dek_and_rek.setGeometry(QtCore.QRect(602, 80, 131, 28))
        self.pushButton_dek_and_rek.setObjectName("pushButton_dek_and_rek")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_first = QtWidgets.QFrame(self.tab_2)
        self.frame_first.setEnabled(True)
        self.frame_first.setGeometry(QtCore.QRect(0, 0, 761, 521))
        self.frame_first.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_first.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_first.setObjectName("frame_first")
        self.pushButton_recieve_agr = QtWidgets.QPushButton(self.frame_first)
        self.pushButton_recieve_agr.setGeometry(QtCore.QRect(70, 410, 181, 23))
        self.pushButton_recieve_agr.setObjectName("pushButton_recieve_agr")
        self.label_18 = QtWidgets.QLabel(self.frame_first)
        self.label_18.setGeometry(QtCore.QRect(320, 410, 171, 21))
        self.label_18.setObjectName("label_18")
        self.lineEdit_agreement = QtWidgets.QLineEdit(self.frame_first)
        self.lineEdit_agreement.setGeometry(QtCore.QRect(510, 410, 113, 20))
        self.lineEdit_agreement.setObjectName("lineEdit_agreement")
        self.pushButton_select_photo_passport_select_agreement = QtWidgets.QPushButton(self.frame_first)
        self.pushButton_select_photo_passport_select_agreement.setGeometry(QtCore.QRect(630, 410, 31, 23))
        self.pushButton_select_photo_passport_select_agreement.setObjectName("pushButton_select_photo_passport_select_agreement")
        self.pushButton_save_1 = QtWidgets.QPushButton(self.frame_first)
        self.pushButton_save_1.setGeometry(QtCore.QRect(550, 480, 121, 23))
        self.pushButton_save_1.setObjectName("pushButton_save_1")
        self.frame_first_data = QtWidgets.QFrame(self.frame_first)
        self.frame_first_data.setGeometry(QtCore.QRect(20, 10, 651, 381))
        self.frame_first_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_first_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_first_data.setObjectName("frame_first_data")
        self.pushButton_select_photo = QtWidgets.QPushButton(self.frame_first_data)
        self.pushButton_select_photo.setGeometry(QtCore.QRect(270, 320, 31, 23))
        self.pushButton_select_photo.setObjectName("pushButton_select_photo")
        self.label_5 = QtWidgets.QLabel(self.frame_first_data)
        self.label_5.setGeometry(QtCore.QRect(0, 150, 151, 20))
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.frame_first_data)
        self.label_14.setGeometry(QtCore.QRect(340, 170, 131, 20))
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.frame_first_data)
        self.label_16.setGeometry(QtCore.QRect(350, 280, 47, 13))
        self.label_16.setObjectName("label_16")
        self.lineEdit_given_by = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_given_by.setGeometry(QtCore.QRect(500, 90, 113, 20))
        self.lineEdit_given_by.setObjectName("lineEdit_given_by")
        self.label_4 = QtWidgets.QLabel(self.frame_first_data)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame_first_data)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 131, 20))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.frame_first_data)
        self.label.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_13 = QtWidgets.QLabel(self.frame_first_data)
        self.label_13.setGeometry(QtCore.QRect(310, 130, 161, 20))
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.frame_first_data)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_phone.setGeometry(QtCore.QRect(150, 190, 113, 20))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.label_15 = QtWidgets.QLabel(self.frame_first_data)
        self.label_15.setGeometry(QtCore.QRect(350, 200, 161, 16))
        self.label_15.setObjectName("label_15")
        self.label_6 = QtWidgets.QLabel(self.frame_first_data)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_email.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_11 = QtWidgets.QLabel(self.frame_first_data)
        self.label_11.setGeometry(QtCore.QRect(420, 60, 47, 13))
        self.label_11.setObjectName("label_11")
        self.lineEdit_pass_number = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_pass_number.setGeometry(QtCore.QRect(500, 60, 113, 20))
        self.lineEdit_pass_number.setObjectName("lineEdit_pass_number")
        self.lineEdit_series = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_series.setGeometry(QtCore.QRect(500, 20, 113, 20))
        self.lineEdit_series.setObjectName("lineEdit_series")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_10 = QtWidgets.QLabel(self.frame_first_data)
        self.label_10.setGeometry(QtCore.QRect(420, 30, 47, 13))
        self.label_10.setObjectName("label_10")
        self.lineEdit_index = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_index.setGeometry(QtCore.QRect(540, 280, 113, 20))
        self.lineEdit_index.setObjectName("lineEdit_index")
        self.pushButton_select_photo_passport = QtWidgets.QPushButton(self.frame_first_data)
        self.pushButton_select_photo_passport.setGeometry(QtCore.QRect(620, 210, 31, 23))
        self.pushButton_select_photo_passport.setObjectName("pushButton_select_photo_passport")
        self.lineEdit_secondname = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_secondname.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.lineEdit_secondname.setObjectName("lineEdit_secondname")
        self.lineEdit_given_date = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_given_date.setGeometry(QtCore.QRect(500, 170, 113, 20))
        self.lineEdit_given_date.setObjectName("lineEdit_given_date")
        self.label_2 = QtWidgets.QLabel(self.frame_first_data)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_adress = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_adress.setGeometry(QtCore.QRect(560, 310, 113, 20))
        self.lineEdit_adress.setObjectName("lineEdit_adress")
        self.lineEdit_photo_passport = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_photo_passport.setGeometry(QtCore.QRect(500, 210, 113, 20))
        self.lineEdit_photo_passport.setObjectName("lineEdit_photo_passport")
        self.lineEdit_code = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_code.setGeometry(QtCore.QRect(500, 130, 113, 20))
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.lineEdit_surname = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_surname.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.lineEdit_photo = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_photo.setGeometry(QtCore.QRect(150, 320, 113, 20))
        self.lineEdit_photo.setObjectName("lineEdit_photo")
        self.label_12 = QtWidgets.QLabel(self.frame_first_data)
        self.label_12.setGeometry(QtCore.QRect(420, 90, 71, 16))
        self.label_12.setObjectName("label_12")
        self.radioButton_hostel = QtWidgets.QRadioButton(self.frame_first_data)
        self.radioButton_hostel.setGeometry(QtCore.QRect(160, 280, 82, 17))
        self.radioButton_hostel.setText("")
        self.radioButton_hostel.setObjectName("radioButton_hostel")
        self.label_9 = QtWidgets.QLabel(self.frame_first_data)
        self.label_9.setGeometry(QtCore.QRect(20, 320, 111, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_birht_date = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_birht_date.setGeometry(QtCore.QRect(150, 150, 113, 20))
        self.lineEdit_birht_date.setObjectName("lineEdit_birht_date")
        self.label_17 = QtWidgets.QLabel(self.frame_first_data)
        self.label_17.setGeometry(QtCore.QRect(350, 310, 191, 16))
        self.label_17.setObjectName("label_17")
        self.label_7 = QtWidgets.QLabel(self.frame_first_data)
        self.label_7.setGeometry(QtCore.QRect(40, 240, 81, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_place_birth = QtWidgets.QLineEdit(self.frame_first_data)
        self.lineEdit_place_birth.setGeometry(QtCore.QRect(150, 240, 113, 20))
        self.lineEdit_place_birth.setObjectName("lineEdit_place_birth")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_second = QtWidgets.QFrame(self.tab_3)
        self.frame_second.setEnabled(True)
        self.frame_second.setGeometry(QtCore.QRect(0, 0, 901, 541))
        self.frame_second.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_second.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_second.setObjectName("frame_second")
        self.pushButton_zayvlenie = QtWidgets.QPushButton(self.frame_second)
        self.pushButton_zayvlenie.setGeometry(QtCore.QRect(380, 350, 141, 23))
        self.pushButton_zayvlenie.setObjectName("pushButton_zayvlenie")
        self.lineEdit_zayavlenie = QtWidgets.QLineEdit(self.frame_second)
        self.lineEdit_zayavlenie.setGeometry(QtCore.QRect(490, 400, 113, 20))
        self.lineEdit_zayavlenie.setObjectName("lineEdit_zayavlenie")
        self.pushButton_select_zayvlenie = QtWidgets.QPushButton(self.frame_second)
        self.pushButton_select_zayvlenie.setGeometry(QtCore.QRect(610, 400, 31, 23))
        self.pushButton_select_zayvlenie.setObjectName("pushButton_select_zayvlenie")
        self.label_28 = QtWidgets.QLabel(self.frame_second)
        self.label_28.setGeometry(QtCore.QRect(380, 400, 111, 16))
        self.label_28.setObjectName("label_28")
        self.pushButton_save_2 = QtWidgets.QPushButton(self.frame_second)
        self.pushButton_save_2.setGeometry(QtCore.QRect(594, 460, 101, 23))
        self.pushButton_save_2.setObjectName("pushButton_save_2")
        self.frame_second_data = QtWidgets.QFrame(self.frame_second)
        self.frame_second_data.setGeometry(QtCore.QRect(10, 0, 641, 311))
        self.frame_second_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_second_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_second_data.setObjectName("frame_second_data")
        self.label_24 = QtWidgets.QLabel(self.frame_second_data)
        self.label_24.setGeometry(QtCore.QRect(10, 280, 121, 16))
        self.label_24.setObjectName("label_24")
        self.pushButton_select_photo_doc_frame2 = QtWidgets.QPushButton(self.frame_second_data)
        self.pushButton_select_photo_doc_frame2.setGeometry(QtCore.QRect(240, 50, 31, 23))
        self.pushButton_select_photo_doc_frame2.setObjectName("pushButton_select_photo_doc_frame2")
        self.lineEdit_math = QtWidgets.QLineEdit(self.frame_second_data)
        self.lineEdit_math.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.lineEdit_math.setObjectName("lineEdit_math")
        self.label_31 = QtWidgets.QLabel(self.frame_second_data)
        self.label_31.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_31.setObjectName("label_31")
        self.lineEdit_IR_or_phys = QtWidgets.QLineEdit(self.frame_second_data)
        self.lineEdit_IR_or_phys.setGeometry(QtCore.QRect(130, 280, 113, 20))
        self.lineEdit_IR_or_phys.setObjectName("lineEdit_IR_or_phys")
        self.lineEdit_number_of_doc_frame_2 = QtWidgets.QLineEdit(self.frame_second_data)
        self.lineEdit_number_of_doc_frame_2.setGeometry(QtCore.QRect(120, 10, 113, 20))
        self.lineEdit_number_of_doc_frame_2.setObjectName("lineEdit_number_of_doc_frame_2")
        self.comboBox_form_of_edu = QtWidgets.QComboBox(self.frame_second_data)
        self.comboBox_form_of_edu.setGeometry(QtCore.QRect(130, 100, 69, 22))
        self.comboBox_form_of_edu.setObjectName("comboBox_form_of_edu")
        self.lineEdit_rus = QtWidgets.QLineEdit(self.frame_second_data)
        self.lineEdit_rus.setGeometry(QtCore.QRect(120, 230, 113, 20))
        self.lineEdit_rus.setObjectName("lineEdit_rus")
        self.lineEdit_achivement_photo = QtWidgets.QLineEdit(self.frame_second_data)
        self.lineEdit_achivement_photo.setGeometry(QtCore.QRect(480, 70, 113, 20))
        self.lineEdit_achivement_photo.setObjectName("lineEdit_achivement_photo")
        self.comboBox_achivements = QtWidgets.QComboBox(self.frame_second_data)
        self.comboBox_achivements.setGeometry(QtCore.QRect(540, 30, 69, 22))
        self.comboBox_achivements.setObjectName("comboBox_achivements")
        self.label_21 = QtWidgets.QLabel(self.frame_second_data)
        self.label_21.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.label_21.setObjectName("label_21")
        self.pushButton_select_photo_doc_frame_select_achivement_photo = QtWidgets.QPushButton(self.frame_second_data)
        self.pushButton_select_photo_doc_frame_select_achivement_photo.setGeometry(QtCore.QRect(600, 70, 31, 23))
        self.pushButton_select_photo_doc_frame_select_achivement_photo.setObjectName("pushButton_select_photo_doc_frame_select_achivement_photo")
        self.label_23 = QtWidgets.QLabel(self.frame_second_data)
        self.label_23.setGeometry(QtCore.QRect(10, 240, 47, 13))
        self.label_23.setObjectName("label_23")
        self.radioButton_educ_frame_2 = QtWidgets.QRadioButton(self.frame_second_data)
        self.radioButton_educ_frame_2.setGeometry(QtCore.QRect(551, 120, 51, 20))
        self.radioButton_educ_frame_2.setText("")
        self.radioButton_educ_frame_2.setObjectName("radioButton_educ_frame_2")
        self.label_27 = QtWidgets.QLabel(self.frame_second_data)
        self.label_27.setGeometry(QtCore.QRect(370, 120, 151, 16))
        self.label_27.setObjectName("label_27")
        self.comboBox_educ_way = QtWidgets.QComboBox(self.frame_second_data)
        self.comboBox_educ_way.setGeometry(QtCore.QRect(130, 150, 69, 22))
        self.comboBox_educ_way.setObjectName("comboBox_educ_way")
        self.lineEdit_select_photo_of_doc = QtWidgets.QLineEdit(self.frame_second_data)
        self.lineEdit_select_photo_of_doc.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit_select_photo_of_doc.setObjectName("lineEdit_select_photo_of_doc")
        self.label_22 = QtWidgets.QLabel(self.frame_second_data)
        self.label_22.setGeometry(QtCore.QRect(10, 190, 81, 16))
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(self.frame_second_data)
        self.label_20.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_20.setObjectName("label_20")
        self.label_25 = QtWidgets.QLabel(self.frame_second_data)
        self.label_25.setGeometry(QtCore.QRect(370, 30, 151, 16))
        self.label_25.setObjectName("label_25")
        self.label_19 = QtWidgets.QLabel(self.frame_second_data)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_19.setObjectName("label_19")
        self.label_26 = QtWidgets.QLabel(self.frame_second_data)
        self.label_26.setGeometry(QtCore.QRect(370, 70, 61, 16))
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_29.setText(_translate("MainWindow", "Добро пожаловать в личный Кабинет"))
        self.pushButton_change_pass.setText(_translate("MainWindow", "Сменить пароль"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Звание"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Контакты"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Предмет"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Фото"))
        self.label_30.setText(_translate("MainWindow", "Факультет"))
        self.label_32.setText(_translate("MainWindow", "Направление"))
        self.pushButton_raspisanie.setText(_translate("MainWindow", "Расписание"))
        self.pushButton_dek_and_rek.setText(_translate("MainWindow", "Деканат и ректорат"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Кабинет"))
        self.pushButton_recieve_agr.setText(_translate("MainWindow", "Получить согласие на обработку"))
        self.label_18.setText(_translate("MainWindow", "Загрузить согласие на обработку"))
        self.pushButton_select_photo_passport_select_agreement.setText(_translate("MainWindow", "..."))
        self.pushButton_save_1.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_select_photo.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "Дата рождения (мм-дд-гггг)"))
        self.label_14.setText(_translate("MainWindow", "Дата выдачи (мм-дд-гггг)"))
        self.label_16.setText(_translate("MainWindow", "Индекс"))
        self.label_4.setText(_translate("MainWindow", "email"))
        self.label_8.setText(_translate("MainWindow", "Нужно ли общежитые"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_13.setText(_translate("MainWindow", "код подразделения (***-***)"))
        self.label_3.setText(_translate("MainWindow", "Отчество"))
        self.label_15.setText(_translate("MainWindow", "фотоскан первой страницы"))
        self.label_6.setText(_translate("MainWindow", "Номер телофона"))
        self.label_11.setText(_translate("MainWindow", "Номер"))
        self.label_10.setText(_translate("MainWindow", "Серия"))
        self.pushButton_select_photo_passport.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_12.setText(_translate("MainWindow", "кем выдан"))
        self.label_9.setText(_translate("MainWindow", "фото на личное дело"))
        self.label_17.setText(_translate("MainWindow", "Адрес(город, улица, дом, квартира)"))
        self.label_7.setText(_translate("MainWindow", "Место рожения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "1 этап"))
        self.pushButton_zayvlenie.setText(_translate("MainWindow", "Получить заявление"))
        self.pushButton_select_zayvlenie.setText(_translate("MainWindow", "..."))
        self.label_28.setText(_translate("MainWindow", "Загрузить заявление"))
        self.pushButton_save_2.setText(_translate("MainWindow", "Сохранить"))
        self.label_24.setText(_translate("MainWindow", "Информатика/физика"))
        self.pushButton_select_photo_doc_frame2.setText(_translate("MainWindow", "..."))
        self.label_31.setText(_translate("MainWindow", "НАправление"))
        self.label_21.setText(_translate("MainWindow", "Форма обучения"))
        self.pushButton_select_photo_doc_frame_select_achivement_photo.setText(_translate("MainWindow", "..."))
        self.label_23.setText(_translate("MainWindow", "Русский"))
        self.label_27.setText(_translate("MainWindow", "Подаю оригинал документа"))
        self.label_22.setText(_translate("MainWindow", "Математика"))
        self.label_20.setText(_translate("MainWindow", "Фото/скан"))
        self.label_25.setText(_translate("MainWindow", "Индивидуальное достижение"))
        self.label_19.setText(_translate("MainWindow", "Номер документа"))
        self.label_26.setText(_translate("MainWindow", "Фото/скан"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "2 этап"))
