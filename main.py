from enter import Ui_MainWindow
from work_with_app import Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets
import time

import sqlite3
import os

import docxtpl


class UI_Task2(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None):
        parent.setDisabled(True)
        self.parent = parent
        super(UI_Task2, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Dialog')

        self.frame_second.hide()
        self.frame_first.hide()
        self.pushButton_change_data.clicked.connect(self.first_page)

        self.pushButton_next.clicked.connect(self.next_page)
        self.pushButton_back.clicked.connect(self.prev_page)
        self.pushButton_commit.clicked.connect(self.commit)

        self.pushButton_recieve_agr.clicked.connect(self.printf)

        self.pushButton_zayvlenie.clicked.connect(self.printf_2)

        self.comboBox_form_of_edu.addItems(["бюджет", "платное"])
        self.comboBox_educ_way.addItems(["Информационных технологий", "Сети и системы связи"])

        self.comboBox_achivements.addItems(["Олимпиада"])

    def check_second(self):
        return True
        if self.lineEdit_number_of_doc_frame_2.text().isdigit():
            pass
        else:
            return False

        if len(self.lineEdit_select_photo_of_doc.text()) > 1:
            pass
        else:
            return False

        if self.comboBox_form_of_edu.currentText():
            pass
        else:
            return False

        if self.comboBox_educ_way.currentText():
            pass
        else:
            return False


        if self.comboBox_achivements.currentText():
            pass
        else:
            return False

        if self.lineEdit_math.text().isdigit():
            pass
        else:
            return False

        if self.lineEdit_rus.text().isdigit():
            pass
        else:
            return False

        if self.lineEdit_IR_or_phys.text().isdigit():
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
                    doc = docxtpl.DocxTemplate("data/шаблон.docx")
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
        return True
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

        if "+" in self.lineEdit_phone.text():
            if self.lineEdit_phone.text()[1:].isdigit():
                pass
            else:
                return False
        elif self.lineEdit_phone.text().isdigit():
            pass
        else:
            return False

        if "".join(self.lineEdit_series.text().split(" ")).isdigit() and len("".join(self.lineEdit_series.text().split(" "))) == 4:
            self.lineEdit_series.setText("".join(self.lineEdit_series.text().split(" ")))
        else:
            return False

        if self.lineEdit_pass_number.text().isdigit() and len("".join(self.lineEdit_pass_number.text().split(" "))) == 6:
            pass
        else:
            return False

        if "-" in self.lineEdit_code.text():
            a = self.lineEdit_code.text().split("-")
            if len(a[0]) == len(a[1]) == 3 and a[0].isdigit() and a[1].isdigit():
                pass
        else:
            return False

        try:
            date = self.lineEdit_given_date.text()
            valid_date = time.strptime(date, '%m-%d-%Y')
        except ValueError:
            return False

        if self.lineEdit_index.text().isdigit():
            pass
        else:
            return False

        return True



    def printf(self):
        # проверка валидности и распечатка
        try:
            if self.check_first():
                doc = docxtpl.DocxTemplate("data/шаблон1.docx")
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

    def commit(self):
        self.frame_second.hide()
        self.frame_greeting.show()

        # все данные первой страницы проверены и готовы


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
        self.update_data()
        email = self.lineEdit_email_enter.text()
        password = self.lineEdit_2.text()
        flag = False
        for i in self.data:
            if email in i and password in i:
                flag = True
                user = i
        if flag:
            mainWindow2 = UI_Task2(self)
            mainWindow2.show()
        else:
            QMessageBox.information(self, 'Ошибка', "Неверный логин или пароль", QMessageBox.Ok)

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
    mainWindow = UI_Task1("data/bd")
    mainWindow.show()
    sys.exit(app.exec())
