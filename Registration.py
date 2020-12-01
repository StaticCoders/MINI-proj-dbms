# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistrationMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import date
from HomePage import *
from main import *

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="amigobong",
    database="bitsfinal"
)


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        # RegistrationWindow.setWindowState(QtCore.Qt.WindowMaximized)
        RegistrationWindow.resize(1416, 834)
        # RegistrationWindow.setWindowState(QtCore.Qt.WindowMaximized)
        RegistrationWindow.setWindowTitle("Registration")
        # Registration.setWindowIcon(QtGui.QIcon('BITS.ico'))
        RegistrationWindow.setMinimumSize(QtCore.QSize(1111, 0))
        RegistrationWindow.setStyleSheet("QMainWindow{\n"
                                          "background-color: rgb(0, 0, 0);\n"
                                          "}\n"
                                          "QLabel#copyrightLabel{\n"
                                          "text-align:center;\n"
                                          "}\n"
                                          "QLabel{\n"
                                          "font: 75 12pt \"Microsoft YaHei\";\n"
                                          "font: 75 12pt \"Microsoft JhengHei UI\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "color: rgb(238, 238, 238);\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit{\n"
                                          "background-color: rgb(238, 238, 238);\n"
                                          "padding: 5px;\n"
                                          "border:2px solid grey;\n"
                                          "border-radius: 4px;\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "border:3px solid #892cdc;\n"
                                          "}\n"
                                          "QLineEdit:focus{\n"
                                          "border:3px solid #892cdc;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "QTextEdit{\n"
                                          "background-color: rgb(238, 238, 238);\n"
                                          "border:2px solid grey;\n"
                                          "border-radius: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit:focus{\n"
                                          "border:3px solid #892cdc;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit:hover{\n"
                                          "border:3px solid #892cdc;\n"
                                          "}\n"
                                          "")
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.registerLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le 12")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.registerLabel.setFont(font)
        self.registerLabel.setStyleSheet("color: rgb(188, 111, 241);\n"
                                         "font: 75 40pt \"Microsoft Tai Le\" bold;\n"
                                         "text-align: center;\n"
                                         "color: rgb(137, 44, 220);\n"
                                         "color: rgb(50, 224, 196);\n"
                                         "color: rgb(188, 111, 241);")
        self.registerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registerLabel.setObjectName("registerLabel")
        self.verticalLayout_4.addWidget(self.registerLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fNameIp = QtWidgets.QLineEdit(self.centralwidget)
        self.fNameIp.setMinimumSize(QtCore.QSize(300, 40))
        self.fNameIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fNameIp.setFont(font)
        self.fNameIp.setStyleSheet("")
        self.fNameIp.setObjectName("fNameIp")
        self.verticalLayout.addWidget(self.fNameIp)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.mNameIp = QtWidgets.QLineEdit(self.centralwidget)
        self.mNameIp.setMinimumSize(QtCore.QSize(300, 40))
        self.mNameIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mNameIp.setFont(font)
        self.mNameIp.setObjectName("mNameIp")
        self.verticalLayout.addWidget(self.mNameIp)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lNameIp = QtWidgets.QLineEdit(self.centralwidget)
        self.lNameIp.setMinimumSize(QtCore.QSize(300, 40))
        self.lNameIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lNameIp.setFont(font)
        self.lNameIp.setObjectName("lNameIp")
        self.verticalLayout.addWidget(self.lNameIp)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.addressIp = QtWidgets.QTextEdit(self.centralwidget)
        self.addressIp.setMinimumSize(QtCore.QSize(300, 87))
        self.addressIp.setMaximumSize(QtCore.QSize(300, 87))
        self.warningLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.warningLabel.setFont(font)
        self.warningLabel.setObjectName("warningLabel")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addressIp.setFont(font)
        self.addressIp.setObjectName("addressIp")
        self.verticalLayout.addWidget(self.addressIp)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.phoneIp = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneIp.setMinimumSize(QtCore.QSize(300, 40))
        self.phoneIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phoneIp.setFont(font)
        self.phoneIp.setObjectName("phoneIp")
        self.verticalLayout_2.addWidget(self.phoneIp)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.educationIp = QtWidgets.QLineEdit(self.centralwidget)
        self.educationIp.setMinimumSize(QtCore.QSize(300, 40))
        self.educationIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.educationIp.setFont(font)
        self.educationIp.setObjectName("educationIp")
        self.verticalLayout_2.addWidget(self.educationIp)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.experienceIp = QtWidgets.QLineEdit(self.centralwidget)
        self.experienceIp.setMinimumSize(QtCore.QSize(300, 40))
        self.experienceIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.experienceIp.setFont(font)
        self.experienceIp.setObjectName("experienceIp")
        self.verticalLayout_2.addWidget(self.experienceIp)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem9)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.referralIp = QtWidgets.QLineEdit(self.centralwidget)
        self.referralIp.setMinimumSize(QtCore.QSize(300, 40))
        self.referralIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.referralIp.setFont(font)
        self.referralIp.setObjectName("referralIp")
        self.verticalLayout_2.addWidget(self.referralIp)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.coursesListView = QtWidgets.QListView(self.centralwidget)
        self.coursesListView.setMinimumSize(QtCore.QSize(311, 188))
        self.coursesListView.setMaximumSize(QtCore.QSize(311, 188))
        self.coursesListView.setStyleSheet("\n"
                                           "QListView{\n"
                                           "padding:3px;\n"
                                           "background-color: rgb(238, 238, 238);\n"
                                           "border: 2px solid grey;\n"
                                           "border-radius: 5px\n"
                                           "}\n"
                                           "QListView:hover{\n"
                                           "border:3px solid #892cdc;\n"
                                           "}")
        self.coursesListView.setObjectName("coursesListView")
        self.verticalLayout_3.addWidget(self.coursesListView)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setMinimumSize(QtCore.QSize(181, 51))
        self.registerButton.setMaximumSize(QtCore.QSize(181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.registerButton.setFont(font)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.registerButton.setStyleSheet("QPushButton{\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border: 2px solid #bc6ff1;\n"
                                          "border-radius: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border: 4px solid #bc6ff1;\n"
                                          "}")
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout_3.addWidget(self.registerButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(181, 51))
        self.closeButton.setMaximumSize(QtCore.QSize(181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.closeButton.setStyleSheet("QPushButton{\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 2px solid red;\n"
                                       "border-radius: 25px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 4px solid red;\n"
                                       "}")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 3)
        spacerItem17 = QtWidgets.QSpacerItem(17, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem17, 2, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 0, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(170, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 0, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(17, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem20, 2, 1, 1, 1)
        self.copyrightLabel = QtWidgets.QLabel(self.centralwidget)
        self.copyrightLabel.setStyleSheet("text-align:center;")
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.gridLayout.addWidget(self.copyrightLabel, 2, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem21, 1, 2, 1, 1)
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)
        self.verticalLayout_4.addWidget(self.warningLabel)
        self.warningLabel.setStyleSheet("QLabel#warningLabel{color: red;}")
        self.warningLabel.hide()

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

        # INPUT VALIDATOR
        # ----String----#
        self.myregex = QtCore.QRegExp("[A-Za-z]+")
        self.myregex3 = QtCore.QRegExp("[A-Za-z ]+")
        self.myregex2 = QtCore.QRegExp("[0-9A-Za-z, -]+")
        self.myregexph = QtCore.QRegExp("[0-9]+")

        self.fNameIp.textChanged.connect(self.validate_inputf)
        self.mNameIp.textChanged.connect(self.validate_inputm)
        self.lNameIp.textChanged.connect(self.validate_inputl)
        self.educationIp.textChanged.connect(self.validate_inputed)
        self.experienceIp.textChanged.connect(self.validate_inputex)
        self.referralIp.textChanged.connect(self.validate_inputre)
        self.phoneIp.textChanged.connect(self.validate_inputph)

        # ----Phone Number----#
        self.onlyInt = QtGui.QIntValidator()
        self.phoneIp.setValidator(self.onlyInt)

        # BUTTON CALLS
        # self.closeButton.clicked.connect(self.CloseWindow)
        # self.registerButton.clicked.connect(self.registerStudent)

        # Adding Courses to ListView
        self.model = QtGui.QStandardItemModel(self.coursesListView)
        self.coursesListView.setModel(self.model)
        courses = []
        mycursor = mydb.cursor()
        mycursor.execute("SELECT course_name FROM courses")
        result = mycursor.fetchall()
        for x in result:
            courses.append(x[0])
        mycursor.close()

        for x in courses:
            item = QtGui.QStandardItem(x)
            item.setCheckable(True)
            self.model.appendRow(item)


    # USER DEFINED FUNCTIONS
    def validate_inputf(self):
        my_validator = QtGui.QRegExpValidator(self.myregex, self.fNameIp)
        self.fNameIp.setValidator(my_validator)

    def validate_inputm(self):
        my_validator = QtGui.QRegExpValidator(self.myregex, self.mNameIp)
        self.mNameIp.setValidator(my_validator)

    def validate_inputl(self):
        my_validator = QtGui.QRegExpValidator(self.myregex, self.lNameIp)
        self.lNameIp.setValidator(my_validator)

    def validate_inputed(self):
        my_validator = QtGui.QRegExpValidator(self.myregex2, self.educationIp)
        self.educationIp.setValidator(my_validator)

    def validate_inputex(self):
        my_validator = QtGui.QRegExpValidator(self.myregex2, self.experienceIp)
        self.experienceIp.setValidator(my_validator)

    def validate_inputre(self):
        my_validator = QtGui.QRegExpValidator(self.myregex3, self.referralIp)
        self.referralIp.setValidator(my_validator)

    def validate_inputph(self):
        my_validator = QtGui.QRegExpValidator(self.myregexph, self.phoneIp)
        self.phoneIp.setValidator(my_validator)


    # def registerStudent(self):
    #     fname = self.fNameIp.text()
    #     mname = self.mNameIp.text()
    #     lname = self.lNameIp.text()
    #     phone = self.phoneIp.text()
    #     address = self.addressIp.toPlainText()
    #     education = self.educationIp.text()
    #     experience = self.experienceIp.text()
    #     referral = self.referralIp.text()
    #     i = 0
    #     mycursor = mydb.cursor()
    #     if fname == "" or mname == "" or lname == "" or phone == "" or address == "" or education == "":
    #         self.warningLabel.show()
    #     else:
    #         tdate = date.today()
    #         sql = "INSERT INTO student_info (first_name,middle_name,last_name,date_of_admission,phone,address," \
    #               "education,experience,referral) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    #         val = (fname, mname, lname, tdate, phone, address, education, experience, referral)
    #         mycursor.execute(sql, val)
    #         if mycursor.rowcount == 1:
    #             print("Data inserted successfully!")
    #         else:
    #             print("Problem occurred while inserting data")
    #         mydb.commit()
    #         getid = "select student_id from student_info order by student_id desc limit 1;"
    #         mycursor.execute(getid)
    #         result = mycursor.fetchone()
    #         courseChecked = []
    #         while self.model.item(i):
    #             if self.model.item(i).checkState():
    #                 courseChecked.append(self.model.item(i).text())
    #             i += 1
    #         i = 0
    #         for x in courseChecked:
    #             sql = "SELECT course_id FROM courses WHERE course_name = \"" + x + "\""
    #             mycursor.execute(sql)
    #             courseid = mycursor.fetchone()
    #             sql = "INSERT INTO student_batch_course(student_id, course_id) VALUES(%s,%s)"
    #             val = (result[0], courseid[0])
    #             mycursor.execute(sql, val)
    #             if mycursor.rowcount == 1:
    #                 print("Data inserted successfully!")
    #             else:
    #                 print("Problem occurred while inserting data")
    #             mydb.commit()
    #             self.fNameIp.clear()
    #             self.mNameIp.clear()
    #             self.lNameIp.clear()
    #             self.phoneIp.clear()
    #             self.addressIp.clear()
    #             self.educationIp.clear()
    #             self.experienceIp.clear()
    #             self.referralIp.clear()



    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "MainWindow"))
        self.registerLabel.setText(_translate("RegistrationWindow", "<strong>REGISTRATION</strong>"))
        self.label.setText(_translate("RegistrationWindow", "First Name:"))
        self.label_2.setText(_translate("RegistrationWindow", "Middle Name:"))
        self.label_3.setText(_translate("RegistrationWindow", "Last Name:"))
        self.label_5.setText(_translate("RegistrationWindow", "Address:"))
        self.warningLabel.setText(_translate("RegistrationWindow", "All the inputs are Mandatory*"))
        self.label_4.setText(_translate("RegistrationWindow", "Phone:"))
        self.label_6.setText(_translate("RegistrationWindow", "Education:"))
        self.label_7.setText(_translate("RegistrationWindow", "Experience:"))
        self.label_8.setText(_translate("RegistrationWindow", "Referral:"))
        self.label_10.setText(_translate("RegistrationWindow", "Courses:"))
        self.registerButton.setText(_translate("RegistrationWindow", "Register"))
        self.closeButton.setText(_translate("RegistrationWindow", "Close"))
        self.copyrightLabel.setText(_translate("RegistrationWindow", "Copyright© 2020 All rights reserved"))

