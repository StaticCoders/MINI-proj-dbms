# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registeration.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import date

from PyQt5.QtWidgets import QCompleter

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="bitsfinal"
)

class Ui_NewRegistrationWindow(object):
    def setupUi(self, RegisterationWindow):
        RegisterationWindow.setObjectName("RegisterationWindow")
        RegisterationWindow.resize(1416, 834)
        RegisterationWindow.setMinimumSize(QtCore.QSize(1111, 0))
        RegisterationWindow.setStyleSheet("QMainWindow{\n"
                                          "background-color: #212121;\n"
                                          "}\n"
                                          "\n"
                                          "QLabel#copyrightLabel{\n"
                                          "text-align:center;\n"
                                          "}\n"
                                          "\n"
                                          "QLabel#registrationLabel{\n"
                                          "color: rgb(50, 224, 196);\n"
                                          "}\n"
                                          "QLabel{\n"
                                          "color: rgb(238, 238, 238);\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit{\n"
                                          "padding: 5px;\n"
                                          "border:2px solid #0d7377;\n"
                                          "border-radius: 4px;\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "border:3px solid #32e0c4;\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit:focus{\n"
                                          "border:3px solid #32e0c4;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit{\n"
                                          "border:2px solid #0d7377;\n"
                                          "border-radius: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit:focus{\n"
                                          "border:3px solid #32e0c4;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit:hover{\n"
                                          "border:3px solid #32e0c4;\n"
                                          "}\n"
                                          "\n"
                                          "QListView{\n"
                                          "border: 2px solid #0d7377;\n"
                                          "border-radius: 5px\n"
                                          "}\n"
                                          "QListView:hover{\n"
                                          "border:3px solid #32e0c4;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton{\n"
                                          "background-color: #212121;\n"
                                          "Color: #eeeeee;\n"
                                          "border-radius: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#registerButton{\n"
                                          "border: 2px solid #0d7377;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#registerButton:hover{\n"
                                          "border: 3px solid #32e0c4;\n"
                                          "background-color: #0d7377;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#cancelButton{\n"
                                          "border: 2px solid #9a0002;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#cancelButton:hover{\n"
                                          "border: 3px solid rgb(255, 0, 0);\n"
                                          "background-color: #9a0002;\n"
                                          "}\n"
                                          "")
        self.centralwidget = QtWidgets.QWidget(RegisterationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.registrationLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.registrationLabel.setFont(font)
        self.registrationLabel.setStyleSheet("")
        self.registrationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registrationLabel.setObjectName("registrationLabel")
        self.verticalLayout_4.addWidget(self.registrationLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fnameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fnameLabel.setFont(font)
        self.fnameLabel.setObjectName("fnameLabel")
        self.verticalLayout.addWidget(self.fnameLabel)
        self.fNameIp = QtWidgets.QLineEdit(self.centralwidget)
        self.fNameIp.setMinimumSize(QtCore.QSize(300, 40))
        self.fNameIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fNameIp.setFont(font)
        self.fNameIp.setStyleSheet("")
        self.fNameIp.setClearButtonEnabled(True)
        self.fNameIp.setObjectName("fNameIp")
        self.verticalLayout.addWidget(self.fNameIp)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.mnameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mnameLabel.setFont(font)
        self.mnameLabel.setObjectName("mnameLabel")
        self.verticalLayout.addWidget(self.mnameLabel)
        self.mNameIp = QtWidgets.QLineEdit(self.centralwidget)
        self.mNameIp.setMinimumSize(QtCore.QSize(300, 40))
        self.mNameIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mNameIp.setFont(font)
        self.mNameIp.setClearButtonEnabled(True)
        self.mNameIp.setObjectName("mNameIp")
        self.verticalLayout.addWidget(self.mNameIp)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.lnameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lnameLabel.setFont(font)
        self.lnameLabel.setObjectName("lnameLabel")
        self.verticalLayout.addWidget(self.lnameLabel)
        self.lNameIp = QtWidgets.QLineEdit(self.centralwidget)
        self.lNameIp.setMinimumSize(QtCore.QSize(300, 40))
        self.lNameIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lNameIp.setFont(font)
        self.lNameIp.setClearButtonEnabled(True)
        self.lNameIp.setObjectName("lNameIp")
        self.verticalLayout.addWidget(self.lNameIp)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.verticalLayout.addWidget(self.addressLabel)
        self.addressIp = QtWidgets.QTextEdit(self.centralwidget)
        self.addressIp.setMinimumSize(QtCore.QSize(300, 87))
        self.addressIp.setMaximumSize(QtCore.QSize(300, 87))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addressIp.setFont(font)
        self.addressIp.setObjectName("addressIp")
        self.verticalLayout.addWidget(self.addressIp)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.phoneLabel.setFont(font)
        self.phoneLabel.setObjectName("phoneLabel")
        self.verticalLayout_2.addWidget(self.phoneLabel)
        self.phoneIp = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneIp.setMinimumSize(QtCore.QSize(300, 40))
        self.phoneIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phoneIp.setFont(font)
        self.phoneIp.setClearButtonEnabled(True)
        self.phoneIp.setObjectName("phoneIp")
        self.verticalLayout_2.addWidget(self.phoneIp)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.educationLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.educationLabel.setFont(font)
        self.educationLabel.setObjectName("educationLabel")
        self.verticalLayout_2.addWidget(self.educationLabel)
        self.educationIp = QtWidgets.QLineEdit(self.centralwidget)
        self.educationIp.setMinimumSize(QtCore.QSize(300, 40))
        self.educationIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.educationIp.setFont(font)
        self.educationIp.setClearButtonEnabled(True)
        self.educationIp.setObjectName("educationIp")
        self.verticalLayout_2.addWidget(self.educationIp)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem9)
        self.experienceLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.experienceLabel.setFont(font)
        self.experienceLabel.setObjectName("experienceLabel")
        self.verticalLayout_2.addWidget(self.experienceLabel)
        self.experienceIp = QtWidgets.QLineEdit(self.centralwidget)
        self.experienceIp.setMinimumSize(QtCore.QSize(300, 40))
        self.experienceIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.experienceIp.setFont(font)
        self.experienceIp.setClearButtonEnabled(True)
        self.experienceIp.setObjectName("experienceIp")
        self.verticalLayout_2.addWidget(self.experienceIp)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem10)
        self.referralLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.referralLabel.setFont(font)
        self.referralLabel.setObjectName("referralLabel")
        self.verticalLayout_2.addWidget(self.referralLabel)
        self.referralIp = QtWidgets.QLineEdit(self.centralwidget)
        self.referralIp.setMinimumSize(QtCore.QSize(300, 40))
        self.referralIp.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.referralIp.setFont(font)
        self.referralIp.setClearButtonEnabled(True)
        self.referralIp.setObjectName("referralIp")
        self.verticalLayout_2.addWidget(self.referralIp)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout_3.addWidget(self.emailLabel)
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setMinimumSize(QtCore.QSize(300, 40))
        self.emailInput.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.emailInput.setFont(font)
        self.emailInput.setClearButtonEnabled(True)
        self.emailInput.setObjectName("emailInput")
        self.verticalLayout_3.addWidget(self.emailInput)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem13)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.coursesListView = QtWidgets.QListView(self.centralwidget)
        self.coursesListView.setMinimumSize(QtCore.QSize(311, 191))
        self.coursesListView.setMaximumSize(QtCore.QSize(311, 191))
        self.coursesListView.setStyleSheet("")
        self.coursesListView.setObjectName("coursesListView")
        self.verticalLayout_3.addWidget(self.coursesListView)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setMinimumSize(QtCore.QSize(181, 50))
        self.registerButton.setMaximumSize(QtCore.QSize(181, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.registerButton.setFont(font)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.registerButton.setStyleSheet("")
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout_3.addWidget(self.registerButton)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(181, 51))
        self.cancelButton.setMaximumSize(QtCore.QSize(181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cancelButton.setStyleSheet("QPushButton{\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 2px solid red;\n"
                                        "border-radius: 25px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 4px solid red;\n"
                                        "}")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 3)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 1, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(17, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem20, 2, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(17, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem21, 2, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(170, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 0, 4, 1, 1)
        RegisterationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterationWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterationWindow.setStatusBar(self.statusbar)
        self.warningLabel = QtWidgets.QLabel(self.centralwidget)
        self.warningLabel.setFont(font)
        self.warningLabel.setObjectName("warningLabel")
        self.verticalLayout_4.addWidget(self.warningLabel)
        self.warningLabel.setStyleSheet("QLabel#warningLabel{color: red;}")
        self.warningLabel.hide()

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
        self.registerButton.clicked.connect(self.registerStudent)

        # Adding Courses to ListView
        self.model = QtGui.QStandardItemModel(self.coursesListView)
        self.coursesListView.setModel(self.model)
        courses = []
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT course_name FROM courses_table")
        result = mycursor.fetchall()
        for x in result:
            courses.append(x[0])

        mycursor.execute("SELECT first_name,middle_name,last_name FROM student_info_table")
        studentList = mycursor.fetchall()
        if len(studentList) != 0:
            lst = [' '.join(x) for x in studentList]
        else:
            lst = []
        completer = QCompleter(lst, self.referralIp)
        self.referralIp.setCompleter(completer)
        mycursor.close()

        for x in courses:
            item = QtGui.QStandardItem(x)
            item.setCheckable(True)
            self.model.appendRow(item)

        self.retranslateUi(RegisterationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterationWindow)

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


    def registerStudent(self):
        fname = self.fNameIp.text()
        mname = self.mNameIp.text()
        lname = self.lNameIp.text()
        phone = self.phoneIp.text()
        address = self.addressIp.toPlainText()
        education = self.educationIp.text()
        experience = self.experienceIp.text()
        referral = self.referralIp.text()
        email = self.emailInput.text()
        i = 0
        mycursor = mydb.cursor(buffered=True)
        if fname == "" or mname == "" or lname == "" or phone == "" or address == "" or education == "":
            self.warningLabel.show()
        else:
            tdate = date.today()
            sql = "INSERT INTO student_info_table(first_name,middle_name,last_name,phone,email,date_of_admission,address,education,experience,referrals) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (fname, mname, lname, phone, email, tdate, address, education, experience, referral)
            print(val)
            mycursor.execute(sql, val)
            if mycursor.rowcount == 1:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Registration Successful!")
                msg.setWindowTitle("Successful!!")
                msg.exec_()

            mydb.commit()
            getid = "select student_id from student_info_table order by student_id desc limit 1;"
            mycursor.execute(getid)
            result = mycursor.fetchone()
            courseChecked = []
            while self.model.item(i):
                if self.model.item(i).checkState():
                    courseChecked.append(self.model.item(i).text())
                i += 1
            i = 0
            for x in courseChecked:
                sql = "SELECT course_id FROM courses_table WHERE course_name = \"" + x + "\""
                mycursor.execute(sql)
                courseid = mycursor.fetchone()
                sql = "INSERT INTO student_course_batch(student_id, course_id) VALUES(%s,%s)"
                val = (result[0], courseid[0])
                mycursor.execute(sql, val)
                mydb.commit()


    def retranslateUi(self, RegisterationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterationWindow.setWindowTitle(_translate("RegisterationWindow", "MainWindow"))
        self.registrationLabel.setText(_translate("RegisterationWindow", "<strong>NEW REGISTRATION</strong>"))
        self.fnameLabel.setText(_translate("RegisterationWindow", "First Name:"))
        self.mnameLabel.setText(_translate("RegisterationWindow", "Middle Name:"))
        self.lnameLabel.setText(_translate("RegisterationWindow", "Last Name:"))
        self.addressLabel.setText(_translate("RegisterationWindow", "Address:"))
        self.phoneLabel.setText(_translate("RegisterationWindow", "Phone:"))
        self.educationLabel.setText(_translate("RegisterationWindow", "Education:"))
        self.experienceLabel.setText(_translate("RegisterationWindow", "Experience(Optional):"))
        self.referralLabel.setText(_translate("RegisterationWindow", "Referral(Optional):"))
        self.emailLabel.setText(_translate("RegisterationWindow", "Email:"))
        self.label_10.setText(_translate("RegisterationWindow", "Courses:"))
        self.registerButton.setText(_translate("RegisterationWindow", "Register"))
        self.cancelButton.setText(_translate("RegisterationWindow", "Cancel"))
        self.warningLabel.setText(_translate("RegistrationWindow", "Fill all the necessary Fields*"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_NewRegistrationWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())