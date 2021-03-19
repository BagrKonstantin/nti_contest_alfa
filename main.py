from enter import Ui_MainWindow
from work_with_app import Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog, QFileDialog
from PyQt5 import QtWidgets, QtGui
import time
from session_2 import UI_Task1 as StaffUi
from session_3 import UI_Task1 as DekanUi
from change_pass import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


import sqlite3
import shutil
import os
from shutil import copy2
import docxtpl


# import pkg_resources.py2_warn


class ChangePassWin(QDialog, Ui_Form):
    def __init__(self, parent=None, *args):
        parent.setDisabled(True)
        super(ChangePassWin, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setWindowTitle("Dialog")
        print(args)
        self.user = args[0]

        self.pushButton.clicked.connect(self.submit)

    def submit(self):
        try:
            if self.user[5] == self.lineEdit_login.text() and self.user[6] == self.lineEdit_old_pass.text():
                if self.lineEdit_new_pass.text() == self.lineEdit_submit_pass.text():
                    con = sqlite3.connect("bd.db")
                    cur = con.cursor()
                    cur.execute(
                        """Update user set password = "{}" where id_user = {}""".format(self.lineEdit_new_pass.text(),
                                                                                        self.user[0]))
                    con.commit()
                    con.close()
                    self.close()
                else:
                    QMessageBox.critical(self, "Ошибка", "Пароли не совпадают", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Ошибка", "Проверьте правильность введённых данных", QMessageBox.Ok)
        except Exception as err:
            print(err)

    def closeEvent(self, event):
        try:
            self.parent.setEnabled(True)
        except Exception as err:
            print(err)


class UI_Task2(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None, *args):
        parent.setDisabled(True)
        self.parent = parent
        super(UI_Task2, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Dialog')

        self.user = args[0]
        print(self.user)

        if self.user[43] == 1:
            self.label_29.setText(
                "Добро пожаловать в личный кабинет студента, \n{} {} {}".format(self.user[2], self.user[1],
                                                                                self.user[3]))
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
            if self.user[33] == 'ПМ':
                con = sqlite3.connect("bd.db")
                cur = con.cursor()
                self.prepod = cur.execute(
                    """Select * from prepodovateli where pm = 1""").fetchall()
                con.close()
            elif self.user[33] == 'ИВТ':
                con = sqlite3.connect("bd.db")
                cur = con.cursor()
                self.prepod = cur.execute(
                    """Select * from prepodovateli where ivt = 1""").fetchall()
                con.close()
            elif self.user[33] == 'АУТС':
                con = sqlite3.connect("bd.db")
                cur = con.cursor()
                self.prepod = cur.execute(
                    """Select * from prepodovateli where ayts = 1""").fetchall()
                con.close()
            elif self.user[33] == 'ИкТ':
                con = sqlite3.connect("bd.db")
                cur = con.cursor()
                self.prepod = cur.execute(
                    """Select * from prepodovateli where ikt = 1""").fetchall()
                con.close()
            elif self.user[33] == 'ЗСС':
                con = sqlite3.connect("bd.db")
                cur = con.cursor()
                self.prepod = cur.execute(
                    """Select * from prepodovateli where zss = 1""").fetchall()
                con.close()
            print(self.prepod)
            self.tableWidget.setRowCount(len(self.prepod))
            self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            self.tableWidget.verticalHeader().setDefaultSectionSize(400)
            for i in range(len(self.prepod)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem())
                self.tableWidget.setItem(i, 1, QTableWidgetItem())
                self.tableWidget.setItem(i, 2, QTableWidgetItem())
                self.tableWidget.setItem(i, 3, QTableWidgetItem())
                self.tableWidget.setItem(i, 4, QTableWidgetItem())
                self.tableWidget.setCellWidget(i, 5, QLabel())

                self.tableWidget.item(i, 0).setText(self.prepod[i][1])
                self.tableWidget.item(i, 1).setText(self.prepod[i][2])
                self.tableWidget.item(i, 2).setText(self.prepod[i][3])
                self.tableWidget.item(i, 3).setText(self.prepod[i][4])
                self.tableWidget.item(i, 4).setText(self.prepod[i][6])
                photo_path = 'prepod_foto/' + str(self.prepod[i][5])
                pixmap = QPixmap(photo_path)
                self.tableWidget.cellWidget(i, 5).setPixmap(pixmap)

            self.lineEdit_fakultet_stud.setText(str(self.user[36]))
            self.lineEdit_napravlenie_stud.setText(str(self.user[33]))
            # self.pushButton_dek_and_rek.clicked.connect()


        else:
            self.frame.hide()
            self.label_29.setText(
                "Добро пожаловать в личный кабинет абитуриента, \n{} {} {}".format(self.user[2], self.user[1],
                                                                                   self.user[3]))
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, True)

            self.lineEdit_surname.setText(self.user[2])
            self.lineEdit_name.setText(self.user[1])
            self.lineEdit_secondname.setText(self.user[3])
            self.lineEdit_email.setText(self.user[5])

            self.lineEdit_series.setValidator(QtGui.QIntValidator(0, 1000))
            self.lineEdit_pass_number.setValidator(QtGui.QIntValidator(0, 100000))
            self.lineEdit_index.setValidator(QtGui.QIntValidator(0, 10000000))

            self.lineEdit_phone.setInputMask("+7(###)-###-##-##)")
            self.lineEdit_code.setInputMask("###-###")
            self.lineEdit_given_date.setInputMask("##-##-####")
            self.lineEdit_birht_date.setInputMask("##-##-####")

            self.pushButton_save_1.clicked.connect(self.save_page_1)
            self.pushButton_save_2.clicked.connect(self.save_page_2)

            self.pushButton_recieve_agr.clicked.connect(self.printf)

            self.pushButton_zayvlenie.clicked.connect(self.printf_2)

            self.comboBox_form_of_edu.addItems(["бюджет", "платное"])
            self.comboBox_educ_way.addItems(["ПМ", "ИВТ", "АУТС", "ИкТ", "ЗСС"])

            self.comboBox_achivements.addItems(["Олимпиада"])

            self.lineEdit_email.setText(str(self.user[5]))
            # password
            self.lineEdit_birht_date.setText(str(self.user[7]))
            self.lineEdit_phone.setText(str(self.user[8]))
            self.lineEdit_place_birth.setText(str(self.user[9]))
            self.radioButton_hostel.setChecked(True if self.user[10] else False)
            # фото
            self.lineEdit_series.setText(str(self.user[12]))
            self.lineEdit_pass_number.setText(str(self.user[13]))
            self.lineEdit_given_by.setText(str(self.user[14]))
            self.lineEdit_code.setText(str(self.user[15]))
            self.lineEdit_given_date.setText(str(self.user[16]))
            # фото паспорт
            self.lineEdit_adress.setText(str(self.user[18]))
            # фото согласие
            self.lineEdit_number_of_doc_frame_2.setText(str(self.user[20]))
            # фото аттестат
            # self.comboBox_form_of_edu.setCurrentIndex(0 if int(self.user[22]) else 1)
            self.lineEdit_rus.setText(str(self.user[23]))
            self.lineEdit_math.setText(str(self.user[24]))
            self.lineEdit_IR_or_phys.setText(str(self.user[25]))
            self.lineEdit_IR_or_phys.setText(str(self.user[26]))
            # self.comboBox_achivements.setCurrentIndex(int(self.user[27]) if self.user[27] else 0)
            self.lineEdit_index.setText(str(self.user[34]))
        # self.comboBox_educ_way.setText(str(self.user[33]))
        # фото достижение

        # self.user_photo_path_1 = 'user_photos/' + self.user[11]
        # self.pixmap = QPixmap(self.user_photo_path_1)
        # self.user_photo.setPixmap(self.pixmap)

        self.lineEdit_photo_passport.setText('passports/' + self.user[17] if self.user[17] else "")
        #
        self.lineEdit_select_photo_of_doc.setText('passports/' + self.user[17] if self.user[17] else "")
        # self.first_page_path_2 = 'passports/' + self.user[17]
        # self.pixmap = QPixmap(self.first_page_path_2)
        # self.first_page.setPixmap(self.pixmap)
        #
        self.lineEdit_agreement.setText('agreements/' + self.user[19] if self.user[19] else "")
        #
        self.lineEdit_zayavlenie.setText('attestats/' + self.user[21] if self.user[21] else "")
        # self.user_photo_path_4 = 'attestats/' + self.user[21]
        # self.pixmap = QPixmap(self.user_photo_path_4)
        # self.document.setPixmap(self.pixmap)
        self.lineEdit_achivement_photo.setText('achiev/' + self.user[28] if self.user[28] else "")
        # self.user_photo_path_5 = 'achiev/' + self.user[28]
        # self.pixmap = QPixmap(self.user_photo_path_5)
        # self.personal_achiev.setPixmap(self.pixmap)

        self.pushButton_change_pass.clicked.connect(self.change_pass)


    def passport(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать фото', '')[0]
        self.lineEdit_photo_passport.setText(fname)

    def agreement(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать фото', '')[0]
        self.lineEdit_agreement.setText(fname)

    def doc(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать фото', '')[0]
        self.lineEdit_select_photo_of_doc.setText(fname)

    def achiv(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать фото', '')[0]
        self.lineEdit_achivement_photo.setText(fname)

    def zayv(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать фото', '')[0]
        self.lineEdit_zayavlenie.setText(fname)

    def change_pass(self):
        try:
            win = ChangePassWin(self, self.user)
            win.show()
        except Exception as err:
            print(err)

    def check_second(self):

        if len(self.lineEdit_select_photo_of_doc.text()) > 1:
            pass
        else:
            return False

        if len(self.lineEdit_achivement_photo.text()) > 1:
            pass
        else:
            return False

        return True

    def printf_2(self):
        try:
            if self.check_second():
                try:
                    doc = docxtpl.DocxTemplate("шаблон.docx")
                    context = {
                        "Имя": self.lineEdit_name.text(),
                        "Фамилия": self.lineEdit_surname.text(),
                        "Отчество": self.lineEdit_secondname.text(),
                        "Серия": self.lineEdit_series.text(),
                        "Номер": self.lineEdit_pass_number.text(),
                        "Дата": self.lineEdit_given_date.text(),
                        "Выданкем": self.lineEdit_given_by.text(),
                        "Специальность": self.comboBox_educ_way.currentText(),
                        "Формаобуч": self.comboBox_form_of_edu.currentText(),

                    }
                    doc.render(context)
                    doc.save('Заявление о зачислении.docx')

                    os.startfile('Заявление о зачислении.docx')
                except Exception as error:
                    print(error)
            else:
                QMessageBox.critical(self, "Ошибка", "Проверьте правильность введённых данных", QMessageBox.Ok)
        except Exception as error:
            print(error)

    def check_first(self):
        if self.lineEdit_surname.text().isalpha():
            pass
        else:
            return False

        if self.lineEdit_name.text().isalpha():
            pass
        else:
            return False

        if self.lineEdit_secondname.text().isalpha():
            pass
        else:
            return False

        if self.lineEdit_place_birth.text().isalpha():
            pass
        else:
            return False

        if len(self.lineEdit_photo.text()) > 1:
            pass
        else:
            return False

        if self.lineEdit_given_by.text().isalpha():
            pass
        else:
            return False

        if len(self.lineEdit_photo_passport.text()) > 1:
            pass
        else:
            return False

        if len(self.lineEdit_adress.text()) > 5:
            pass
        else:
            return False

        if "@" in self.lineEdit_email.text() and "." in self.lineEdit_email.text():
            pass
        else:
            return False

        try:
            date = self.lineEdit_birht_date.text()
            valid_date = time.strptime(date, '%m-%d-%Y')
        except ValueError:
            return False

        try:
            date = self.lineEdit_given_date.text()
            valid_date = time.strptime(date, '%m-%d-%Y')
        except ValueError:
            return False

        return True

    def printf(self):
        pass
        # проверка валидности и распечатка
        try:
            if self.check_first():
                doc = docxtpl.DocxTemplate("шаблон1.docx")
                context = {
                    "Имя": self.lineEdit_name.text(),
                    "Фамилия": self.lineEdit_surname.text(),
                    "Отчество": self.lineEdit_secondname.text(),
                    "Серия": self.lineEdit_series.text(),
                    "Номер": self.lineEdit_pass_number.text(),
                    "Дата": self.lineEdit_given_date.text(),

                }
                doc.render(context)
                doc.save('СОГЛАСИЕ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ.docx')

                os.startfile('СОГЛАСИЕ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ.docx')


            else:
                QMessageBox.critical(self, "Ошибка", "Проверьте правильность введённых данных", QMessageBox.Ok)
        except Exception as error:
            print(error)

    def save_page_1(self):
        try:

            data = [self.lineEdit_name.text(), self.lineEdit_surname.text(), self.lineEdit_secondname.text(),
                    self.lineEdit_email.text(), self.lineEdit_birht_date.text(), self.lineEdit_phone.text(),
                    self.lineEdit_place_birth.text(), self.radioButton_hostel.isChecked(), self.lineEdit_photo.text(),
                    self.lineEdit_series.text(), self.lineEdit_pass_number.text(), self.lineEdit_given_by.text(),
                    self.lineEdit_code.text(), self.lineEdit_given_date.text(), self.lineEdit_photo_passport.text(),
                    self.lineEdit_index.text(), self.lineEdit_adress.text(), self.lineEdit_agreement.text()]
            print(os.getcwd() + "/passports/" + self.lineEdit_photo_passport.text().split("/")[-1])
            copy2('{}'.format(self.lineEdit_photo_passport.text()), os.getcwd() + "/passports/" + self.lineEdit_photo_passport.text().split("/")[-1])
            copy2('{}'.format(self.lineEdit_agreement.text()), os.getcwd() + "/agreements/" + self.lineEdit_agreement.text().split("/")[-1])


            con = sqlite3.connect("bd.db")
            cur = con.cursor()
            cur.execute("""update user set (user_name, user_surname, user_secondname,
                                        email, birthday, telephone, birthplace,
                                            hostel, user_photo, passport_seria,
                                             passport_number, passport_kem_vidan, passport_kod_podrazdelenia,
                                              passport_date, passport_photo, pochta_index, adress_living, agreement) =
                                               ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}") where id_user = {}""".format(
                *data, self.user[0]))
            con.commit()
            con.close()
        except Exception as err:
            print(err)

    def save_page_2(self):
        try:
            data = [self.lineEdit_number_of_doc_frame_2.text(), self.lineEdit_select_photo_of_doc.text(),
                    self.comboBox_form_of_edu.currentText(),
                    self.comboBox_educ_way.currentText(), self.lineEdit_math.text(), self.lineEdit_rus.text(),
                    self.lineEdit_IR_or_phys.text(),
                    self.lineEdit_fiz_ege.text(),
                    self.comboBox_achivements.currentText(), self.lineEdit_achivement_photo.text(),
                    self.comboBox_educ_way.isEnabled(),
                    self.pushButton_zayvlenie.text()]

            copy2(self.lineEdit_select_photo_of_doc.text(), os.getcwd() + "/attestats/" + self.lineEdit_select_photo_of_doc.text().split("/")[-1])
            copy2(self.lineEdit_achivement_photo.text(), os.getcwd() + "/achiev/" + self.lineEdit_achivement_photo.text().split("/")[-1])
            copy2(self.lineEdit_zayavlenie.text(), os.getcwd() + "/user_photos/" + self.lineEdit_zayavlenie.text().split("/")[-1])

            con = sqlite3.connect("bd.db")
            cur = con.cursor()
            cur.execute("""update user set (attestat_number, attestat_photo, form_of_education, napravlenie,
                                            ege_mat, ege_rus, ege_inf, ege_fis, achiev_title, achiev_photo, 
                                            document_original, agreement) = ("{}", "{}", "{}", "{}", "{}", "{}", "{}", 
                                            "{}", "{}", "{}", "{}", "{}") where id_user = {}""".format(*data,
                                                                                                       self.user[0]))
            con.commit()
            con.close()
            print('xxxx')
        except Exception as err:
            print(err)

    def first_page(self):
        self.frame_greeting.hide()
        self.frame_first.show()

    def next_page(self):
        self.frame_first.hide()
        self.frame_second.show()
        # все данные готовы

    def prev_page(self):
        self.frame_first.show()
        self.frame_second.hide()

    def closeEvent(self, event):
        self.parent.setDisabled(False)


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path

        self.t = 1

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select * from user""").fetchall()
        con.close()
        self.pushButton_re_enter.clicked.connect(self.swap)
        self.swap()

        self.pushButton_female.clicked.connect(self.swap_fem)
        self.pushButton_male.clicked.connect(self.swap_man)
        self.pushButton_female.setEnabled(False)

        self.pushButton_enter.clicked.connect(self.open_tab)

        self.pushButton_reg.clicked.connect(self.reg_user)

    def update_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select * from user""").fetchall()
        con.close()

    def reg_user(self):
        try:
            if not ("@" in self.lineEdit_mail.text() and "." in self.lineEdit_mail.text()):
                QMessageBox.information(self, 'Ошибка', "Невалидный email", QMessageBox.Ok)
                return
            user_data = [self.lineEdit_name.text(), self.lineEdit_surname.text(), self.lineEdit_sec_name.text()]
            if self.pushButton_female.isEnabled():
                user_data.append(0)
            else:
                user_data.append(1)
            user_data.append(self.lineEdit_mail.text())
            user_data.append(self.lineEdit_password.text())
            self.update_data()
            flag = True
            for i in self.data:
                if user_data[4] in i:
                    flag = False
            if flag:
                con = sqlite3.connect(self.path)
                cur = con.cursor()
                cur.execute(
                    """insert into user (user_name, user_surname, user_secondname, sex, email, password) values 
                    ("{}", "{}", "{}", {}, "{}", "{}")""".format(*user_data))
                con.commit()
                con.close()
            else:
                QMessageBox.information(self, 'Ошибка', "Такой пользователь уже существует", QMessageBox.Ok)
            print(user_data)
            self.swap()
        except Exception as err:
            print(err)

    def open_tab(self):
        try:
            self.update_data()
            email = self.lineEdit_email_enter.text()
            password = self.lineEdit_2.text()
            flag = False
            staff_flag = False
            dekanat_flag = False
            con = sqlite3.connect(self.path)
            cur = con.cursor()
            staff = cur.execute("""Select * from staff""").fetchall()
            dekanat = cur.execute("""Select * from dekanat""").fetchall()
            con.close()
            for i in self.data:
                if email == i[5] and password == i[6]:
                    flag = True
                    user = i
            for i in staff:
                if email == i[1] and password == i[2]:
                    staff_flag = True
            for i in dekanat:
                if email == i[1] and password == i[2]:
                    dekanat_flag = True
                    user = i
            if flag:
                mainWindow2 = UI_Task2(self, user)
                mainWindow2.show()
            elif staff_flag:
                self.mainWindow3 = StaffUi(self.path)
                self.mainWindow3.show()
            elif dekanat_flag:
                self.win = DekanUi(self.path, user)
                self.win.show()
            else:
                QMessageBox.information(self, 'Ошибка', "Неверный логин или пароль", QMessageBox.Ok)
        except Exception as err:
            print(err)

    def swap(self):
        self.t *= -1
        if self.t > 0:
            self.frame_enter.hide()
            self.frame_reg.show()
        else:
            self.frame_enter.show()
            self.frame_reg.hide()

    def swap_fem(self):
        self.pushButton_male.setEnabled(True)
        self.pushButton_female.setEnabled(False)

    def swap_man(self):
        self.pushButton_male.setEnabled(False)
        self.pushButton_female.setEnabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
