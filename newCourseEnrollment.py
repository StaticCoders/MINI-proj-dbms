# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newCourseEnrollment.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QCompleter

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="amigobong",
    database="bitsfinal"
)


class Ui_NewCourseEnrollmentWindow(object):
    def setupUi(self, NewCourseEnrollmentWindow):
        NewCourseEnrollmentWindow.setObjectName("NewCourseEnrollmentWindow")
        NewCourseEnrollmentWindow.resize(1052, 651)
        NewCourseEnrollmentWindow.setStyleSheet("QDialog{\n"
                                                "background-color: #212121;\n"
                                                "}\n"
                                                "\n"
                                                "QLabel{\n"
                                                "color: #eeeeee;\n"
                                                "}\n"
                                                "\n"
                                                "QLabel#newCourseEnrollLabel{\n"
                                                "color: #32e0c4;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit{\n"
                                                "padding-left: 6px;\n"
                                                "padding-right: 6px;\n"
                                                "border: 2px solid #0d7377;\n"
                                                "border-radius: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit:hover{\n"
                                                "border: 3px solid #32e0c4;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit:focus{\n"
                                                "border: 3px solid #32e0c4;\n"
                                                "}\n"
                                                "\n"
                                                "QListWidget{\n"
                                                "border: 2px solid #0d7377;\n"
                                                "border-radius: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QListWidget:hover{\n"
                                                "border: 3px solid #32e0c4;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton{\n"
                                                "background-color: #212121;\n"
                                                "Color: #eeeeee;\n"
                                                "border-radius: 20px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton#submitButton{\n"
                                                "border: 2px solid #0d7377;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton#submitButton:hover{\n"
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
                                                "}")
        self.gridLayout = QtWidgets.QGridLayout(NewCourseEnrollmentWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.newCourseEnrollLabel = QtWidgets.QLabel(NewCourseEnrollmentWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.newCourseEnrollLabel.setFont(font)
        self.newCourseEnrollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newCourseEnrollLabel.setObjectName("newCourseEnrollLabel")
        self.gridLayout.addWidget(self.newCourseEnrollLabel, 1, 0, 1, 3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.studentLabel = QtWidgets.QLabel(NewCourseEnrollmentWindow)
        self.studentLabel.setMinimumSize(QtCore.QSize(332, 40))
        self.studentLabel.setMaximumSize(QtCore.QSize(332, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.studentLabel.setFont(font)
        self.studentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.studentLabel.setObjectName("studentLabel")
        self.verticalLayout_2.addWidget(self.studentLabel)
        self.nameInput = QtWidgets.QLineEdit(NewCourseEnrollmentWindow)
        self.nameInput.setMinimumSize(QtCore.QSize(332, 40))
        self.nameInput.setMaximumSize(QtCore.QSize(332, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameInput.setFont(font)
        self.nameInput.setText("")
        self.nameInput.setClearButtonEnabled(True)
        self.nameInput.setObjectName("nameInput")
        self.verticalLayout_2.addWidget(self.nameInput)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.coursesLabel = QtWidgets.QLabel(NewCourseEnrollmentWindow)
        self.coursesLabel.setMinimumSize(QtCore.QSize(332, 40))
        self.coursesLabel.setMaximumSize(QtCore.QSize(332, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.coursesLabel.setFont(font)
        self.coursesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coursesLabel.setObjectName("coursesLabel")
        self.verticalLayout.addWidget(self.coursesLabel)
        self.courseList = QtWidgets.QListWidget(NewCourseEnrollmentWindow)
        self.courseList.setMinimumSize(QtCore.QSize(332, 280))
        self.courseList.setMaximumSize(QtCore.QSize(332, 280))
        self.courseList.setObjectName("courseList")
        self.verticalLayout.addWidget(self.courseList)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submitButton = QtWidgets.QPushButton(NewCourseEnrollmentWindow)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 40))
        self.submitButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout.addWidget(self.submitButton)
        self.cancelButton = QtWidgets.QPushButton(NewCourseEnrollmentWindow)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 40))
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT first_name,middle_name,last_name FROM student_info_table")
        studentList = mycursor.fetchall()
        if len(studentList) != 0:
            lst = [' '.join(x) for x in studentList]
        else:
            lst = []
        completer = QCompleter(lst, self.nameInput)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        self.nameInput.setCompleter(completer)
        mycursor.execute("SELECT course_name FROM courses_table")
        result = mycursor.fetchall()
        courses = []
        count = 0
        for x in result:
            self.courseList.addItem(x[0])
            self.courseList.item(count).setCheckState(QtCore.Qt.Unchecked)
            count += 1
        mycursor.close()
        self.submitButton.clicked.connect(self.enrollForCourse)

        self.retranslateUi(NewCourseEnrollmentWindow)
        QtCore.QMetaObject.connectSlotsByName(NewCourseEnrollmentWindow)

    def enrollForCourse(self):
        if self.nameInput.text() == "" or self.courseList.count() == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please select name and courses before Submitting")
            msg.setWindowTitle("Warning")
            msg.exec_()
        else:
            mycursor = mydb.cursor(buffered=True)
            name = self.nameInput.text()
            name = name.strip()
            name = tuple(name.split(" "))
            if(len(name) < 3):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Invalid Name Input")
                msg.setInformativeText("Name field should contain first name, middle name and last name of the student")
                msg.setWindowTitle("Warning")
                msg.exec_()
            elif(len(name)>3):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Invalid Name Input")
                msg.setInformativeText("Name field should contain first name, middle name and last name of the student")
                msg.setWindowTitle("Warning")
                msg.exec_()
            else:
                sql = "SELECT student_id FROM student_info_table WHERE first_name = (%s) AND middle_name = (%s) AND last_name = (%s)"
                mycursor.execute(sql, name)
                getSID = mycursor.fetchone()
                if mycursor.rowcount == 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Either Person is not Registered or name is Incorrect")
                    msg.setWindowTitle("Warning")
                    msg.exec_()
                else:
                    courses = []
                    c = 0
                    k = 0
                    for x in range(self.courseList.count()):
                        if self.courseList.item(x).checkState():
                            courses.append(self.courseList.item(x).text())
                    for i in courses:
                        sql = "SELECT course_id FROM courses_table WHERE course_name = '" + i + "'"
                        mycursor.execute(sql)
                        getCID = mycursor.fetchone()
                        sql = "SELECT student_id,course_id FROM student_course_batch WHERE course_id = (%s) AND student_id = (%s)"
                        val = (getCID[0], getSID[0])
                        mycursor.execute(sql, val)
                        if mycursor.rowcount != 0:
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Information)
                            msg.setText("The student has already opted for the course "+i)
                            msg.setWindowTitle("Information")
                            k += 1
                            msg.exec_()
                        else:
                            sql = "INSERT INTO student_course_batch (student_id, course_id) VALUES(%s,%s)"
                            val = (getSID[0], getCID[0])
                            mycursor.execute(sql, val)
                            mydb.commit()
                        c += 1
                    print(k)
                    print(len(courses))
                    if len(courses) == c and k < len(courses):
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        if len(courses) == c and k == 1:
                            msg.setText("Successfully Enrolled for New course")
                        else:
                            msg.setText("Successfully Enrolled for New courses")
                        msg.setWindowTitle("Success")
                        msg.exec_()
                        self.nameInput.clear()
                        for x in range(self.courseList.count()):
                            if self.courseList.item(x).checkState():
                               self.courseList.item(x).setCheckState(QtCore.Qt.Unchecked)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText("Enrollment Not Completed")
                        msg.setInformativeText("Please select courses which are not opted by the student earlier")
                        msg.setWindowTitle("Warning")
                        msg.exec_()



    def retranslateUi(self, NewCourseEnrollmentWindow):
        _translate = QtCore.QCoreApplication.translate
        NewCourseEnrollmentWindow.setWindowTitle(_translate("NewCourseEnrollmentWindow", "Dialog"))
        self.newCourseEnrollLabel.setText(_translate("NewCourseEnrollmentWindow", "NEW COURSE ENROLLMENT"))
        self.studentLabel.setText(_translate("NewCourseEnrollmentWindow", "Search Student\'s Name"))
        self.coursesLabel.setText(_translate("NewCourseEnrollmentWindow", "Select Courses"))
        self.submitButton.setText(_translate("NewCourseEnrollmentWindow", "Submit"))
        self.cancelButton.setText(_translate("NewCourseEnrollmentWindow", "Cancel"))
