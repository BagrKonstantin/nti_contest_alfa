from enter import Ui_MainWindow
from work_with_app import  Ui_MainWindow as Ui_MainWindow2
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

        self.pushButton_next.clicked.connect(self.next_page)

        self.frame_second.hide()



    def next_page(self):
        self.frame_first.hide()
        self.frame_second.show()


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path

        self.t = 1

        # con = sqlite3.connect(self.path)
        # cur = con.cursor()
        # self.data = cur.execute("""Select * from users""").fetchall()
        # con.close()
        self.pushButton_re_enter.clicked.connect(self.swap)
        self.swap()

        self.pushButton_female.clicked.connect(self.swap_fem)
        self.pushButton_male.clicked.connect(self.swap_man)
        self.pushButton_female.setEnabled(False)

        self.pushButton_enter.clicked.connect(self.open_tab)

        self.pushButton_reg.clicked.connect(self.reg_user)

    def reg_user(self):
        data = [self.lineEdit_name.text(), self.lineEdit_surname.text(), self.lineEdit_sec_name.text()]
        if self.pushButton_female.isEnabled():
            data.append(0)
        else:
            data.append(1)
        data.append(self.lineEdit_email_enter.text())
        data.append(self.lineEdit_password.text())
        print(data)



    def open_tab(self):
        mainWindow2 = UI_Task2(self)
        mainWindow2.show()


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
    mainWindow = UI_Task1("../data.db")
    mainWindow.show()
    sys.exit(app.exec())
