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
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path

        self.tableWidget.cellClicked.connect(self.open_tab)
        self.tableWidget.setRowCount(1)

        self.tableWidget.setItem(0, 0, QTableWidgetItem())
        self.tableWidget.item(0, 0).setText("  sdg")


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
                dialog = Dialog(self, num=self.tableWidget.verticalHeader().sortIndicatorSection())
                dialog.show()
                print("no error")
            except Exception as error:
                print(error)



class Dialog(QMainWindow, Dialog_ui):
    def __init__(self, parent=None, num=None):
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
    mainWindow = UI_Task1("data/bd")
    mainWindow.show()
    sys.exit(app.exec())
