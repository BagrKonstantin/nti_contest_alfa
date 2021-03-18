from stud_card import Ui_MainWindow as Dialog_ui
from decan_vision import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
import time
from PyQt5.QtWidgets import *
import sqlite3
import os

import docxtpl
#import pkg_resources.py2_warn


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path, *args):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path
        self.user = args[0]
        print(self.user)

        self.tableWidget_5.cellClicked.connect(self.open_tab)
        if self.user[0] == 0:
            self.comboBox_2.addItems(['', 'ПМ', 'ИВТ', 'АУТС'])
        else:
            self.comboBox_2.addItems(['', 'ИкТ', 'ЗСС'])

        self.pushButton_2.clicked.connect(self.update_table2)
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.update_data()

    def update_table2(self):
        try:
            con = sqlite3.connect(self.path)
            cur = con.cursor()
            data = cur.execute(
                """Select * from user where napravlenie = '{}'""".format(self.comboBox_2.currentText())).fetchall()
            con.close()
            self.tableWidget_5.setRowCount(len(data))
            for i in range(len(data)):
                self.tableWidget_5.setItem(i, 0, QTableWidgetItem())

                # print(sum(data[i][23] + data[i][24] + data[i][25] + data[i][26]))

                self.tableWidget_5.item(i, 0).setText(str(data[i][1] + " " + data[i][2] + " " + data[i][3]))

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
                print(self.data)
                print(self.tableWidget_5.currentRow())
                dialog = Dialog(self, self.data[self.tableWidget_5.currentRow()], self.user)
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

        self.pushButton_2.clicked.connect(self.print)
        self.pushButton_3.clicked.connect(self.print2)
        self.pushButton_4.clicked.connect(self.print3)
        self.data = args[0]
        self.dekan = args[1]
        print(self.data)
        self.lineEdit_name_2.setText(str(self.data[1]))
        self.lineEdit_secondname_2.setText(str(self.data[3]))
        self.lineEdit_surname_2.setText(str(self.data[2]))
        self.lineEdit_sex_2.setText("Мужской" if self.data[4] == 0 else "Женский")
        self.lineEdit_email_2.setText(str(self.data[5]))
        # password
        self.lineEdit_birht_date_2.setText(str(self.data[7]))
        self.lineEdit_phone_2.setText(str(self.data[8]))
        self.lineEdit_place_birth_2.setText(str(self.data[9]))
        # self.radioButton_hostel_2.setChecked(True if self.data[10] else False)
        # фото
        self.lineEdit_series_2.setText(str(self.data[12]))
        self.lineEdit_pass_number_2.setText(str(self.data[13]))
        self.lineEdit_given_by_2.setText(str(self.data[14]))
        self.lineEdit_code_2.setText(str(self.data[15]))
        self.lineEdit_given_date_2.setText(str(self.data[16]))
        # фото паспорт
        self.lineEdit_adress_2.setText(str(self.data[18]))
        # фото согласие
        self.lineEdit_number_of_doc_frame_3.setText(str(self.data[20]))
        # фото аттестат
        self.lineEdit_teach_form.setText("бюджет" if self.data[22] else "платное")
        self.lineEdit_direction.setText(str(self.data[33]))
        self.lineEdit_direction_2.setText(str(self.data[36]))
        # self.lineEdit_group_num.setText(str(self.data[35]))
        self.lineEdit_num_book.setText(str(self.data[37]))
        self.lineEdit_read_ticket.setText(str(self.data[38]))
        self.lineEdit_date_zachis.setText(str(self.data[39]))
        self.lineEdit_date_otchis.setText(str(self.data[40]))
        self.lineEdit_adress_3.setText(str(self.data[41]))
        self.lineEdit_god_postyplenia.setText(str(self.data[42]))

        if self.lineEdit_adress_3.text() == self.lineEdit_adress_2.text():
            print(self.data[41], self.data[17])
            self.lineEdit_adress_3.setReadOnly(True)
            self.lineEdit_adress_2.setReadOnly(True)

        if self.dekan[3] == 0:
            data = ['ПМ1', 'ПМ2', 'ИВТ1', 'ИВТ2', 'АУТС1', 'АУТС2']
            self.comboBox.addItems(data)
            self.comboBox.setCurrentIndex(data.index(self.data[35]))
        else:
            data = ['ИкТ1', 'ИкТ2', 'ИкТ3', 'ЗСС1', 'ЗСС2', 'ЗСС3']

            self.comboBox.addItems(data)
            self.comboBox.setCurrentIndex(data.index(self.data[35]))

        # фото достижение

        self.user_photo_path_1 = 'user_photos/' + self.data[11]
        self.pixmap = QPixmap(self.user_photo_path_1)
        self.user_photo.setPixmap(self.pixmap)

        self.first_page_path_2 = 'passports/' + self.data[17]
        self.pixmap = QPixmap(self.first_page_path_2)
        self.first_page.setPixmap(self.pixmap)

        self.pushButton.clicked.connect(self.back)

        self.pushButton_user.clicked.connect(self.open0)
        self.pushButton_first_page.clicked.connect(self.open1)

        self.data_file = ['user_photos/' + self.data[11], 'passports/' + self.data[17], 'agreements/' + self.data[19],
                          'attestats/' + self.data[21], 'achiev/' + self.data[28]]

    def open0(self):
        print(os.getcwd())
        try:
            os.startfile(os.getcwd() + "/" + self.data_file[0])
        except Exception as err:
            print(err)

    def open1(self):
        os.startfile(os.getcwd() + "/" + self.data_file[1])

    def closeEvent(self, event):
        self.parent.setDisabled(False)

    def back(self):
        data = [self.lineEdit_phone_2.text(), self.lineEdit_email_2.text(), self.lineEdit_adress_2.text(),
                self.lineEdit_adress_3.text()]
        self.close()
        self.parent.setDisabled(False)

    def print3(self):
        try:
            doc = docxtpl.DocxTemplate("Формат студенческого билета.docx")
            context = {
                "Факультет": self.lineEdit_direction_2.text(),
                "Группа": self.comboBox.currentText(),

                "Ф": self.lineEdit_surname_2.text(),
                "И": self.lineEdit_name_2.text(),
                "О": self.lineEdit_secondname_2.text(),

                "Номербилета": self.lineEdit_num_book.text(),
                "year1": "2021",
                "year2": "2022",
                "year3": "2023",
                "year4": "2024",
                "year5": "2025",
                "year6": "2026",
                "level1": "1",
                "level2": "2",
                "level3": "3",
                "level4": "4",
                "level5": "5",
                "level6": "6",

            }
            doc.render(context)
            doc.save('Студенческий билет.docx')

            os.startfile(os.getcwd() + '/Студенческий билет.docx')
        except Exception as err:
            print(err)

    def print2(self):
        try:
            doc = docxtpl.DocxTemplate("Формат зачетной книжки.docx")
            context = {
                "Факультет": self.lineEdit_direction_2.text(),
                "Специальность": self.lineEdit_direction.text(),

                "Ф": self.lineEdit_surname_2.text(),
                "И": self.lineEdit_name_2.text(),
                "О": self.lineEdit_secondname_2.text(),

                "Номеркнижки": self.lineEdit_num_book.text(),

            }
            doc.render(context)
            doc.save('Зачётная книжка.docx')

            os.startfile(os.getcwd() + '/Зачётная книжка.docx')
        except Exception as err:
            print(err)

    def print(self):
        try:
            doc = docxtpl.DocxTemplate("Формат личного дела.docx")
            context = {
                "Факультет": self.lineEdit_direction_2.text(),
                "Специальность": self.lineEdit_direction.text(),
                "Группа": self.lineEdit_group_num.text(),
                "Основа": self.lineEdit_teach_form.text(),
                "Номердела": "",
                "Ф": self.lineEdit_surname_2.text(),
                "И": self.lineEdit_name_2.text(),
                "О": self.lineEdit_secondname_2.text(),
                "Рождение": self.lineEdit_birht_date_2.text(),
                "Место": self.lineEdit_place_birth_2.text(),

                "Серия": self.lineEdit_series_2.text(),
                "Номер": self.lineEdit_pass_number_2.text(),
                "когдавыдан": self.lineEdit_given_date_2.text(),
                "выданкем": self.lineEdit_given_by_2.text(),

                "Телефон": self.lineEdit_phone_2.text(),
                "mail": self.lineEdit_email_2.text(),
                "адрес": self.lineEdit_adress_2.text(),

            }
            doc.render(context)
            doc.save('Личное дело.docx')

            os.startfile(os.getcwd() + '/Личное дело.docx')
        except Exception as err:
            print(err)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db", (1, 'ПупкинВС', 'ПупкинВасилий123', 1))
    mainWindow.show()
    sys.exit(app.exec())
