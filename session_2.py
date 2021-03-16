from personal import Ui_MainWindow as Dialog_ui
from top import Ui_MainWindow
from work_with_app import Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets, QtGui
import time

from PyQt5.QtWidgets import *

import sqlite3
import os


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path, *args):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path
        self.update_data()
        self.update_table()
        self.tableWidget_2.cellClicked.connect(self.open_tab)

    def update_table(self):
        try:
            self.tableWidget_2.setRowCount(len(self.data))
            statuses = ['Новый', 'В работе', 'Комплект без оригинала', 'Полный комплект']
            stadias = ['Новый', 'На рассмотрении', 'Отправлено на доработку', 'Принято']

            for i in range(len(self.data)):
                print(self.data[i])
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem())
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem())
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem())
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem())
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem())
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem())
                self.tableWidget_2.item(i, 0).setText(str(self.data[i][1] + " " + self.data[i][2] + " " + self.data[i][3]))
                self.tableWidget_2.item(i, 1).setText(str(self.data[i][4]))
                self.tableWidget_2.item(i, 2).setText(str(self.data[i][5]))
                self.tableWidget_2.item(i, 3).setText(str(self.data[i][8]))
                self.tableWidget_2.item(i, 4).setText(str(statuses[self.data[i][-2]]))
                self.tableWidget_2.item(i, 5).setText(str(stadias[self.data[i][-1]]))
        except Exception as err:
            print(err)



    def update_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select * from user""").fetchall()
        con.close()


    def open_tab(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        # msg.setIconPixmap(pixmap)  # Своя картинка

        msg.setWindowTitle("Абитуриент")
        msg.setText("Вы хотите посмотреть данные абитуриента?")
        # msg.setInformativeText("Хотите сохранить информацию перед выходом?")

        msg.addButton('Отмена', QMessageBox.YesRole)
        ok_button = msg.addButton('Да', QMessageBox.AcceptRole)
        # close_button = msg.addButton('Закрыть', QMessageBox.RejectRole)

        msg.exec()
        if msg.clickedButton() == ok_button:
            print("opendialog")
            try:
                print(self.tableWidget_2.verticalHeader().sortIndicatorSection())
                dialog = Dialog(self, self.data[self.tableWidget_2.verticalHeader().sortIndicatorSection() - 1])
                dialog.show()
                print("no error")
            except Exception as error:
                print(error)



class Dialog(QMainWindow, Dialog_ui):
    def __init__(self, parent=None, *args):
        parent.setDisabled(True)
        self.parent = parent
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Dialog')




        self.pushButton.clicked.connect(self.back)

    def closeEvent(self, event):
        self.parent.setDisabled(False)



    def back(self):
        self.close()
        self.parent.setDisabled(False)






    def back(self):
        self.close()
        self.parent.setDisabled(False)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
