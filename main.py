from enter import Ui_MainWindow
from work_with_app import Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore

from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
import os


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

    def commit(self):
        self.frame_second.hide()
        self.frame_greeting.show()

    def first_page(self):
        self.frame_greeting.hide()
        self.frame_first.show()

    def next_page(self):
        self.frame_first.hide()
        self.frame_second.show()

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
    mainWindow = UI_Task1("bd")
    mainWindow.show()
    sys.exit(app.exec())
