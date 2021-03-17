from personal import Ui_MainWindow as Dialog_ui
from top import Ui_MainWindow
from work_with_app import Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
import time
from email.mime.text import MIMEText
from PyQt5.QtWidgets import *
import smtplib
import sqlite3
import smtplib
import os


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path
        self.update_data()
        self.update_table()
        self.update_table2()
        self.update_table3()
        self.updata_table_4()
        self.tableWidget_2.cellClicked.connect(self.open_tab)
        self.comboBox.addItems(['', 'ПМ', 'ИВТ', 'АУТС', 'ИкТ', 'ЗСС'])

        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget_3.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget_4.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


        self.pushButton.clicked.connect(self.update_table2)

    def updata_table_4(self):
        try:
            con = sqlite3.connect(self.path)
            cur = con.cursor()
            data = cur.execute(
                """Select * from user where hostel = {}""".format(1)).fetchall()
            con.close()
            self.tableWidget_4.setRowCount(len(data))
            print(data)

            for i in range(len(data)):
                self.tableWidget_4.setItem(i, 0, QTableWidgetItem())
                self.tableWidget_4.setItem(i, 1, QTableWidgetItem())

                self.tableWidget_4.item(i, 0).setText(str(data[i][1] + " " + data[i][2] + " " + data[i][3]))
                if self.data[i][30] == 1:
                    self.tableWidget_4.item(i, 1).setText(str('да'))
                else:
                    self.tableWidget_4.item(i, 1).setText(str('нет'))
        except Exception as err:
            print(err)

    def update_table3(self):
        self.tableWidget_3.setRowCount(len(self.data))

        for i in range(len(self.data)):
            self.tableWidget_3.setItem(i, 0, QTableWidgetItem())
            self.tableWidget_3.setItem(i, 1, QTableWidgetItem())
            self.tableWidget_3.setItem(i, 2, QTableWidgetItem())
            self.tableWidget_3.setItem(i, 3, QTableWidgetItem())

            self.tableWidget_3.item(i, 0).setText(str(self.data[i][1] + " " + self.data[i][2] + " " + self.data[i][3]))
            self.tableWidget_3.item(i, 1).setText(str(self.data[i][23] + self.data[i][24] + self.data[i][25] + self.data[i][26]))
            if self.data[i][29] == 1:
                self.tableWidget_3.item(i, 2).setText('10')
            else:
                self.tableWidget_3.item(i, 2).setText('0')
            if self.data[i][30] == 1:
                self.tableWidget_3.item(i, 3).setText(str('да'))
            else:
                self.tableWidget_3.item(i, 3).setText(str('нет'))

    def update_table2(self):
        try:
            con = sqlite3.connect(self.path)
            cur = con.cursor()
            data = cur.execute("""Select * from user where napravlenie = '{}'""".format(self.comboBox.currentText())).fetchall()
            con.close()
            self.tableWidget.setRowCount(len(data))
            for i in range(len(data)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem())
                self.tableWidget.setItem(i, 1, QTableWidgetItem())
                self.tableWidget.setItem(i, 2, QTableWidgetItem())
                self.tableWidget.setItem(i, 3, QTableWidgetItem())

                # print(sum(data[i][23] + data[i][24] + data[i][25] + data[i][26]))

                self.tableWidget.item(i, 0).setText(str(data[i][1] + " " + data[i][2] + " " + data[i][3]))
                self.tableWidget.item(i, 1).setText(str(data[i][23] + data[i][24] + data[i][25] + data[i][26]))
                if data[i][29] == 1:
                    self.tableWidget.item(i, 2).setText('10')
                else:
                    self.tableWidget.item(i, 2).setText('0')
                if data[i][30] == 1:
                    self.tableWidget.item(i, 3).setText(str('да'))
                else:
                    self.tableWidget.item(i, 3).setText(str('нет'))
        except Exception as err:
            print(err)

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
                self.tableWidget_2.item(i, 0).setText(
                    str(self.data[i][1] + " " + self.data[i][2] + " " + self.data[i][3]))
                self.tableWidget_2.item(i, 1).setText("Мужской" if self.data[i][4] == 0 else "Женский")
                self.tableWidget_2.item(i, 2).setText(str(self.data[i][5]))
                self.tableWidget_2.item(i, 3).setText(str(self.data[i][8]))
                self.tableWidget_2.item(i, 4).setText(str(statuses[self.data[i][-5]]))
                self.tableWidget_2.item(i, 5).setText(str(stadias[self.data[i][-4]]))
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

        # for i, j in enumerate(args[0]):
        #     print(j, i)

        data = args[0]

        self.lineEdit_name_2.setText(str(data[1]))
        self.lineEdit_secondname_2.setText(str(data[2]))
        self.lineEdit_surname_2.setText(str(data[3]))
        self.lineEdit_sex_2.setText("Мужской" if data[4] == 0 else "Женский")
        self.lineEdit_email_2.setText(str(data[5]))
        # password
        self.lineEdit_birht_date_2.setText(str(data[7]))
        self.lineEdit_phone_2.setText(str(data[8]))
        self.lineEdit_place_birth_2.setText(str(data[9]))
        self.radioButton_hostel_2.setChecked(True if data[10] else False)
        # фото
        self.lineEdit_series_2.setText(str(data[12]))
        self.lineEdit_pass_number_2.setText(str(data[13]))
        self.lineEdit_given_by_2.setText(str(data[14]))
        self.lineEdit_code_2.setText(str(data[15]))
        self.lineEdit_given_date_2.setText(str(data[16]))
        # фото паспорт
        self.lineEdit_adress_2.setText(str(data[18]))
        # фото согласие
        self.lineEdit_number_of_doc_frame_3.setText(str(data[20]))
        # фото аттестат
        self.lineEdit_teach_form.setText("бюджет" if data[22] else "платное")
        self.lineEdit_rus_2.setText(str(data[23]))
        self.lineEdit_math_2.setText(str(data[24]))
        self.lineEdit_inf.setText(str(data[25]))
        self.lineEdit_fizika.setText(str(data[26]))
        self.lineEdit_achiev.setText(str(data[27]))
        self.lineEdit_index_2.setText(str(data[34]))
        self.lineEdit_direction.setText(str(data[33]))
        # фото достижение

        self.user_photo_path = 'user_photos/' + data[11]
        self.pixmap = QPixmap(self.user_photo_path)
        self.user_photo.setPixmap(self.pixmap)


        self.first_page_path = 'passports/' + data[17]
        self.pixmap = QPixmap(self.user_photo_path)
        self.first_page.setPixmap(self.pixmap)

        self.user_photo_path = 'agreements/' + data[19]
        self.pixmap = QPixmap(self.user_photo_path)
        self.soglasie_na_zachislenie.setPixmap(self.pixmap)

        self.user_photo_path = 'attestats/' + data[21]
        self.pixmap = QPixmap(self.user_photo_path)
        self.document.setPixmap(self.pixmap)

        self.user_photo_path = 'achiev/' + data[28]
        self.pixmap = QPixmap(self.user_photo_path)
        self.personal_achiev.setPixmap(self.pixmap)



        self.pushButton.clicked.connect(self.back1)

        self.pushButton_user.clicked.connect(self.open0)
        self.pushButton_first_page.clicked.connect(self.open1)
        self.pushButton_sogl.clicked.connect(self.open2)
        self.pushButton_doc.clicked.connect(self.open3)
        self.pushButton_achiv.clicked.connect(self.open4)

        self.data_file = ['user_photos/' + data[11], 'passports/' + data[17], 'agreements/' + data[19], 'attestats/' + data[21], 'achiev/' + data[28]]

    def open0(self):
        print(os.getcwd())
        try:
            os.startfile(os.getcwd() + "/" + self.data_file[0])
        except Exception as err:
            print(err)
    def open1(self):
        os.startfile(os.getcwd() + "/" +  self.data_file[1])
    def open2(self):
        os.startfile(os.getcwd() + "/" + self.data_file[2])
    def open3(self):
        os.startfile(os.getcwd() + "/" + self.data_file[3])
    def open4(self):
        os.startfile(os.getcwd() + "/" + self.data_file[4])

    def closeEvent(self, event):
        self.parent.setDisabled(False)

    def send_message(self, email, message):
        message = message.encode("utf-8")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("info26.sgu@gmail.com",  "aleks321245")
        server.sendmail("info26.sgu@gmail.com", email, message)
        server.quit()



    def back1(self):

        try:
            if self.checkBox.isChecked() or self.checkBox_2.isChecked() or self.checkBox_3.isChecked() or self.checkBox_4.isChecked() or self.checkBox_5.isChecked() or self.checkBox_6.isChecked() or self.checkBox_7.isChecked():
                self.send_message(self.lineEdit_email_2.text(), """Добрый день!
    Уведомляем вас, что вы успешно подали документы в Сызранский государственный университет имени Филиппа Лимонадова. С этого момента вы участвуете в конкурсе на зачисление.
    С уважением,
    приемная комиссия СГУ им. Ф.Лимонадова""")
                # изменение статуса на всё супер
            else:
                self.send_message(self.lineEdit_email_2.text(), """Добрый день!
    Уведомляем вас, что при подаче документов в Сызранский государственный университет имени Филиппа Лимонадова вы допустили ошибки.
    Просим исправить ошибки в ближайшее время.
    С уважением,
    приемная комиссия СГУ им. Ф.Лимонадова”""")
                # изменение статуса на доработать
            print(111111111111111111111111111111111111111111111111111111)
            self.close()
            self.parent.setDisabled(False)

        except Exception as error:
            print(error)



    def back(self):
        self.close()
        self.parent.setDisabled(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
