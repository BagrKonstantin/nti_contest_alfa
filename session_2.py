from execution import Ui_MainWindow
from work_with_app import Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets, QtGui
import time

import sqlite3
import os


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path, *args):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path







if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("data/bd")
    mainWindow.show()
    sys.exit(app.exec())
