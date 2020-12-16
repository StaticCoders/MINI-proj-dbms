# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batchAllotment.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


###### Note #######
# This cde is to be changed and updated.
# A new Table for every Batch is not required so, the code here is to be changed.
###### End Note #######

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="mpdev"
)

class Ui_BatchAllotmentWindow(object):
    def setupUi(self, BatchAllotmentWindow):
        BatchAllotmentWindow.setObjectName("BatchAllotmentWindow")
        BatchAllotmentWindow.resize(1178, 844)
        BatchAllotmentWindow.setStyleSheet("QMainWindow{\n"
                                           "background-color: #212121;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "background-color: #212121;\n"
                                           "Color: #eeeeee;\n"
                                           "border-radius: 20px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#addButton{\n"
                                           "border: 2px solid #0d7377;\n"
                                           "border-radius: 25px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#addButton:hover{\n"
                                           "border: 3px solid #32e0c4;\n"
                                           "background-color: #0d7377;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#submitButton{\n"
                                           "border: 2px solid #0d7377;\n"
                                           "border-radius: 25px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#submitButton:hover{\n"
                                           "border: 3px solid #32e0c4;\n"
                                           "background-color: #0d7377;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#cancelButton{\n"
                                           "color: #eeeeee;\n"
                                           "background-color: #212121;\n"
                                           "border: 2px solid #9a0002;\n"
                                           "border-radius: 25px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#cancelButton:hover{\n"
                                           "border: 3px solid rgb(255, 0, 0);\n"
                                           "background-color: #9a0002;\n"
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
                                           "QTextEdit{\n"
                                           "border: 2px solid #0d7377;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QTextEdit:hover{\n"
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
                                           "QSpinBox{\n"
                                           "border: 2px solid #0d7377;\n"
                                           "}\n"
                                           "\n"
                                           "QSpinBox:hover{\n"
                                           "border: 2px solid #32e0c4;\n"
                                           "}\n"
                                           "\n"
                                           "QLabel{\n"
                                           "color: #eeeeee;\n"
                                           "}\n"
                                           "\n"
                                           "QLabel#batchAllotmentLabel{\n"
                                           "color: #32e0c4;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox{\n"
                                           "border: 2px solid #0d7377;\n"
                                           "border-radius: 5px;\n"
                                           "padding-left: 4px;\n"
                                           "padding-right: 4px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:hover{\n"
                                           "border: 3px solid #32e0c4;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox QAbstractItemView {\n"
                                           "border: 2px solid #32e0c4;\n"
                                           "selection-background-color: #0d7377;\n"
                                           "}\n"
                                           "")
        self.centralwidget = QtWidgets.QWidget(BatchAllotmentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.batchAllotmentLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.batchAllotmentLabel.setFont(font)
        self.batchAllotmentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.batchAllotmentLabel.setObjectName("batchAllotmentLabel")
        self.verticalLayout_5.addWidget(self.batchAllotmentLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectCourseLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectCourseLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.selectCourseLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.selectCourseLabel.setFont(font)
        self.selectCourseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectCourseLabel.setObjectName("selectCourseLabel")
        self.verticalLayout.addWidget(self.selectCourseLabel)
        self.courseComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.courseComboBox.setEnabled(True)
        self.courseComboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.courseComboBox.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.courseComboBox.setFont(font)
        self.courseComboBox.setObjectName("courseComboBox")
        self.verticalLayout.addWidget(self.courseComboBox)
        self.selectBatchLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectBatchLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.selectBatchLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.selectBatchLabel.setFont(font)
        self.selectBatchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectBatchLabel.setObjectName("selectBatchLabel")
        self.verticalLayout.addWidget(self.selectBatchLabel)
        self.batchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.batchComboBox.setEnabled(True)
        self.batchComboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.batchComboBox.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.batchComboBox.setFont(font)
        self.batchComboBox.setObjectName("batchComboBox")
        self.verticalLayout.addWidget(self.batchComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(5, 0))
        self.line.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line.setStyleSheet("background-color: #32e0c4;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchNameLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.searchNameLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.searchNameLabel.setFont(font)
        self.searchNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchNameLabel.setObjectName("searchNameLabel")
        self.verticalLayout_2.addWidget(self.searchNameLabel)
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setMinimumSize(QtCore.QSize(300, 40))
        self.nameInput.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameInput.setFont(font)
        self.nameInput.setText("")
        self.nameInput.setClearButtonEnabled(True)
        self.nameInput.setObjectName("nameInput")
        self.verticalLayout_2.addWidget(self.nameInput)
        self.studentListLabel = QtWidgets.QLabel(self.centralwidget)
        self.studentListLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.studentListLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.studentListLabel.setFont(font)
        self.studentListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.studentListLabel.setWordWrap(True)
        self.studentListLabel.setObjectName("studentListLabel")
        self.verticalLayout_2.addWidget(self.studentListLabel)
        self.studentList = QtWidgets.QListWidget(self.centralwidget)
        self.studentList.setMinimumSize(QtCore.QSize(300, 300))
        self.studentList.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.studentList.setFont(font)
        self.studentList.setDragEnabled(True)
        self.studentList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.studentList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.studentList.setObjectName("studentList")
        self.verticalLayout_2.addWidget(self.studentList)
        self.dragndrop = QtWidgets.QLabel(self.centralwidget)
        self.dragndrop.setMinimumSize(QtCore.QSize(300, 40))
        self.dragndrop.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dragndrop.setFont(font)
        self.dragndrop.setAlignment(QtCore.Qt.AlignCenter)
        self.dragndrop.setObjectName("dragndrop")
        self.verticalLayout_2.addWidget(self.dragndrop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setMinimumSize(QtCore.QSize(5, 0))
        self.line_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_2.setStyleSheet("background-color: #32e0c4;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.studentsAddedListLabel = QtWidgets.QLabel(self.centralwidget)
        self.studentsAddedListLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.studentsAddedListLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.studentsAddedListLabel.setFont(font)
        self.studentsAddedListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.studentsAddedListLabel.setObjectName("studentsAddedListLabel")
        self.verticalLayout_3.addWidget(self.studentsAddedListLabel)
        self.studentsAddedList = QtWidgets.QListWidget(self.centralwidget)
        self.studentsAddedList.setMinimumSize(QtCore.QSize(300, 300))
        self.studentsAddedList.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.studentsAddedList.setFont(font)
        self.studentsAddedList.setDragEnabled(True)
        self.studentsAddedList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.studentsAddedList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.studentsAddedList.setObjectName("studentsAddedList")
        self.verticalLayout_3.addWidget(self.studentsAddedList)
        self.dragndrop2 = QtWidgets.QLabel(self.centralwidget)
        self.dragndrop2.setMinimumSize(QtCore.QSize(300, 40))
        self.dragndrop2.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dragndrop2.setFont(font)
        self.dragndrop2.setAlignment(QtCore.Qt.AlignCenter)
        self.dragndrop2.setObjectName("dragndrop2")
        self.verticalLayout_3.addWidget(self.dragndrop2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setMinimumSize(QtCore.QSize(140, 50))
        self.addButton.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(130, 50))
        self.cancelButton.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)
        BatchAllotmentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BatchAllotmentWindow)
        self.statusbar.setObjectName("statusbar")
        BatchAllotmentWindow.setStatusBar(self.statusbar)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT course_name FROM courses_table")
        result = mycursor.fetchall()
        for x in result:
            self.courseComboBox.addItem(x[0])
        self.courseComboBox.setCurrentIndex(-1)
        self.batchComboBox.setCurrentIndex(-1)
        self.courseComboBox.currentIndexChanged.connect(self.loadBatches)
        self.addButton.clicked.connect(self.addToBatch)
        self.nameInput.textChanged.connect(self.searchInNames)

        self.retranslateUi(BatchAllotmentWindow)
        QtCore.QMetaObject.connectSlotsByName(BatchAllotmentWindow)

    def addToBatch(self):
        mycursor = mydb.cursor(buffered=True)
        curBatch = self.batchComboBox.currentText()
        curCourse = self.courseComboBox.currentText()
        items = []
        globalcert = []
        print(curBatch,curCourse)
        for i in range(self.studentsAddedList.count()):
            items.append(self.studentsAddedList.item(i))
            if self.studentsAddedList.item(i).checkState():
                globalcert.append(self.studentsAddedList.item(i))
        for x in items:
            name = tuple(x.text().split(" "))
            sql = "SELECT batch_id FROM batches_table WHERE batch_name = '" + curBatch + "'"
            mycursor.execute(sql)
            getBatchId = mycursor.fetchone()
            sql = "SELECT course_id FROM courses_table WHERE course_name = '" + curCourse + "'"
            mycursor.execute(sql)
            courseid = mycursor.fetchone()
            sql = "SELECT student_id FROM student_info_table WHERE first_name = (%s) AND middle_name =(%s) AND " \
                  "last_name = (%s) "
            mycursor.execute(sql, name)
            getStudentId = mycursor.fetchone()
            query = "CREATE TABLE IF NOT EXISTS bitsfinal." + curBatch + "(id INT NOT NULL AUTO_INCREMENT, student_id INT NULL, course_id INT NULL, global_cert ENUM('Yes', 'No') NULL, PRIMARY KEY (`id`), FOREIGN KEY (student_id) REFERENCES student_info_table(student_id), FOREIGN KEY (course_id) REFERENCES courses_table(course_id));"
            mycursor.execute(query)
            print(getBatchId,getStudentId,courseid)
            if x in globalcert:
                sql = "UPDATE student_course_batch SET batch_id = (%s), global_cert = 'Yes' WHERE student_id = (%s) " \
                      "AND course_id = (%s)"
                val = (getBatchId[0], getStudentId[0], courseid[0])
                mycursor.execute(sql, val)
                sql = "INSERT INTO " + curBatch + " (student_id,course_id, global_cert) VALUES(%s,%s,%s)"
                val = (getStudentId[0], courseid[0], 'Yes')
                print(val)
                mycursor.execute(sql, val)
            else:
                sql = "UPDATE student_course_batch SET batch_id = (%s), global_cert = 'No' WHERE student_id = (%s) " \
                      "AND course_id = (%s)"
                val = (getBatchId[0], getStudentId[0], courseid[0])
                mycursor.execute(sql, val)
                sql = "INSERT INTO "+curBatch+" (student_id,course_id, global_cert) VALUES(%s,%s,%s)"
                val = (getStudentId[0], courseid[0], 'No')
                print(val)
                mycursor.execute(sql, val)
            mydb.commit()
        print(mycursor.rowcount,len(items))
        if mycursor.rowcount == len(items):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Batch Allotted to selected students")
            msg.setWindowTitle("Successful!!")
            msg.exec_()
            self.courseComboBox.setCurrentIndex(-1)
            self.batchComboBox.setCurrentIndex(-1)
            self.nameInput.clear()
            self.studentList.clear()
            self.studentsAddedList.clear()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Batch Allottment Failed")
            msg.setWindowTitle("Fail")
            msg.exec_()
        mydb.commit()
        mycursor.close()

    def loadBatches(self):
        self.batchComboBox.clear()
        if self.courseComboBox.currentIndex() != -1:
            mycursor = mydb.cursor(buffered=True)
            curCourse = self.courseComboBox.currentText()
            sql = "SELECT course_id FROM courses_table WHERE course_name = '" + curCourse + "'"
            mycursor.execute(sql)
            courseid = mycursor.fetchone()
            sql = "SELECT batch_name FROM batches_table WHERE course_id = " + str(courseid[0])
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for x in result:
                self.batchComboBox.addItem(x[0])
            mycursor.close()
            self.loadNames()

    def searchInNames(self):
        self.studentList.clear()
        searchString = self.nameInput.text()
        curBatch = self.batchComboBox.currentText()
        self.studentList.clear()
        mycursor = mydb.cursor(buffered=True)
        curCourse = self.courseComboBox.currentText()
        sql = "SELECT course_id FROM courses_table WHERE course_name = '" + curCourse + "'"
        mycursor.execute(sql)
        courseid = mycursor.fetchone()
        sql = "SELECT st.first_name, st.middle_name, st.last_name FROM student_info_table st, student_course_batch " \
              "scb WHERE st.student_id = scb.student_id AND scb.course_id = " + str(courseid[0]) + " AND (st.first_name LIKE '%" + searchString + "%' OR st.middle_name LIKE '%" + searchString + "%' OR st.last_name LIKE '%" + searchString + "%')"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        count = 0
        for x in result:
            name = " ".join(x)
            self.studentList.addItem(name)
            self.studentList.item(count).setCheckState(QtCore.Qt.Unchecked)
            count += 1

        mycursor.close()

    def loadNames(self):
        curBatch = self.batchComboBox.currentText()
        self.studentList.clear()
        mycursor = mydb.cursor(buffered=True)
        curCourse = self.courseComboBox.currentText()
        sql = "SELECT course_id FROM courses_table WHERE course_name = '" + curCourse + "'"
        mycursor.execute(sql)
        courseid = mycursor.fetchone()
        sql = "SELECT st.first_name, st.middle_name, st.last_name FROM student_info_table st, student_course_batch " \
              "scb WHERE st.student_id = scb.student_id AND scb.course_id = " + str(courseid[0])
        mycursor.execute(sql)
        result = mycursor.fetchall()
        count = 0
        for x in result:
            name = " ".join(x)
            self.studentList.addItem(name)
            self.studentList.item(count).setCheckState(QtCore.Qt.Unchecked)
            count += 1

        mycursor.close()

    def retranslateUi(self, BatchAllotmentWindow):
        _translate = QtCore.QCoreApplication.translate
        BatchAllotmentWindow.setWindowTitle(_translate("BatchAllotmentWindow", "Student-Batch Allotment"))
        self.batchAllotmentLabel.setText(_translate("BatchAllotmentWindow", "BATCH ALLOTMENT"))
        self.selectCourseLabel.setText(_translate("BatchAllotmentWindow", "Select Course"))
        self.selectBatchLabel.setText(_translate("BatchAllotmentWindow", "Select Batch"))
        self.searchNameLabel.setText(_translate("BatchAllotmentWindow", "Search Student\'s Name"))
        self.studentListLabel.setText(_translate("BatchAllotmentWindow", "Students opted for the selected Course"))
        self.dragndrop.setText(_translate("BatchAllotmentWindow", "Drag and Drop to add to the Batch"))
        self.studentsAddedListLabel.setText(_translate("BatchAllotmentWindow", "Students added to selected Batch"))
        self.dragndrop2.setText(_translate("BatchAllotmentWindow", "Drag and Drop to remove from the Batch"))
        self.addButton.setText(_translate("BatchAllotmentWindow", "Add to Batch"))
        self.cancelButton.setText(_translate("BatchAllotmentWindow", "Cancel"))
