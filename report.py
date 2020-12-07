# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
########### Added Code ##########
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox
import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="amigobong",
                               database="bitsfinal")

########### End of Added Code #######


class Ui_report(object):
    def setupUi(self, report):
        report.setObjectName("report")
        report.resize(993, 715)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(report.sizePolicy().hasHeightForWidth())
        report.setSizePolicy(sizePolicy)
        report.setMinimumSize(QtCore.QSize(480, 360))
        self.centralwidget = QtWidgets.QWidget(report)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(900, 100))
        self.label.setMaximumSize(QtCore.QSize(900, 100))
        font = QtGui.QFont()
        font.setPointSize(49)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(90, 30))
        self.label_2.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.start_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dateEdit.sizePolicy().hasHeightForWidth())
        self.start_dateEdit.setSizePolicy(sizePolicy)
        self.start_dateEdit.setMinimumSize(QtCore.QSize(125, 30))
        self.start_dateEdit.setMaximumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.start_dateEdit.setFont(font)
        self.start_dateEdit.setProperty("showGroupSeparator", False)
        self.start_dateEdit.setCalendarPopup(True)
        self.start_dateEdit.setObjectName("start_dateEdit")
        self.horizontalLayout.addWidget(self.start_dateEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(90, 30))
        self.label_3.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.end_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dateEdit.sizePolicy().hasHeightForWidth())
        self.end_dateEdit.setSizePolicy(sizePolicy)
        self.end_dateEdit.setMinimumSize(QtCore.QSize(125, 30))
        self.end_dateEdit.setMaximumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.end_dateEdit.setFont(font)
        self.end_dateEdit.setCalendarPopup(True)
        self.end_dateEdit.setObjectName("end_dateEdit")
        self.horizontalLayout.addWidget(self.end_dateEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.ok_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_Button.sizePolicy().hasHeightForWidth())
        self.ok_Button.setSizePolicy(sizePolicy)
        self.ok_Button.setMinimumSize(QtCore.QSize(120, 40))
        self.ok_Button.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ok_Button.setFont(font)
        self.ok_Button.setAutoDefault(True)
        self.ok_Button.setObjectName("ok_Button")
        self.horizontalLayout.addWidget(self.ok_Button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(130, 30))
        self.label_4.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.choice_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_tableWidget.sizePolicy().hasHeightForWidth())
        self.choice_tableWidget.setSizePolicy(sizePolicy)
        self.choice_tableWidget.setMinimumSize(QtCore.QSize(361, 351))
        self.choice_tableWidget.setMaximumSize(QtCore.QSize(361, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.choice_tableWidget.setFont(font)
        self.choice_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.choice_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.choice_tableWidget.setAlternatingRowColors(True)
        self.choice_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.choice_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.choice_tableWidget.setObjectName("choice_tableWidget")
        self.choice_tableWidget.setColumnCount(2)
        self.choice_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.choice_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choice_tableWidget.setHorizontalHeaderItem(1, item)
        self.choice_tableWidget.horizontalHeader().setDefaultSectionSize(179)
        self.verticalLayout.addWidget(self.choice_tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(130, 30))
        self.label_5.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.detail_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detail_tableWidget.sizePolicy().hasHeightForWidth())
        self.detail_tableWidget.setSizePolicy(sizePolicy)
        self.detail_tableWidget.setMinimumSize(QtCore.QSize(571, 351))
        self.detail_tableWidget.setMaximumSize(QtCore.QSize(571, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detail_tableWidget.setFont(font)
        self.detail_tableWidget.setAlternatingRowColors(True)
        self.detail_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.detail_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.detail_tableWidget.setObjectName("detail_tableWidget")
        self.detail_tableWidget.setColumnCount(0)
        self.detail_tableWidget.setRowCount(0)
        self.detail_tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.verticalLayout_2.addWidget(self.detail_tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.backHome_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backHome_Button.sizePolicy().hasHeightForWidth())
        self.backHome_Button.setSizePolicy(sizePolicy)
        self.backHome_Button.setMinimumSize(QtCore.QSize(150, 50))
        self.backHome_Button.setMaximumSize(QtCore.QSize(150, 50))
        self.backHome_Button.setObjectName("backHome_Button")
        self.horizontalLayout_3.addWidget(self.backHome_Button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 2, 1, 1, 1)
        report.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(report)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 22))
        self.menubar.setObjectName("menubar")
        report.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(report)
        self.statusbar.setObjectName("statusbar")
        report.setStatusBar(self.statusbar)

        self.retranslateUi(report)
        QtCore.QMetaObject.connectSlotsByName(report)



        ####### Added Code ######

        self.start_dateEdit.setMinimumDate(QDate(2016,1,1)) # 1 Jan 2016 <Minimum date>
        self.end_dateEdit.setMinimumDate(QDate(2016, 1, 1))  # 1 Jan 2016 <Minimum date>
        self.start_dateEdit.dateChanged.connect(self.startDateChanged)
        self.end_dateEdit.dateChanged.connect(self.endDateChanged)
        self.ok_Button.clicked.connect(self.showData)

    def startDateChanged(self): # Date Check
        self.end_dateEdit.setMinimumDate(self.start_dateEdit.date()) # Set the Miniumum date to start date

    def endDateChanged(self): # Date Check
        self.start_dateEdit.setMaximumDate(self.end_dateEdit.date()) # Set the Max date to that of endDate

    def showData(self):
        self.startDate = self.start_dateEdit.date().toString('yyyy-MM-dd')
        self.endDate = self.end_dateEdit.date().toString('yyyy-MM-dd')
        self.showRecordsTable(self.startDate,self.endDate)
        self.choice_tableWidget.currentItemChanged.connect(self.showDetailTable) # Row Clicked, show the details of the row

    def showRecordsTable(self, startDate, endDate):
        # Shows the table where all the records are stored with their total numbers
        self.choice_tableWidget.clear()
        sqls = []                     # All the sql queries are added to this list
        numbers = []                  # all the total numbers for the all the records will be kept in this
        choices = []                  # This stores the list of all the choice fields to be displayed.

        sqls.append("select count(*) from student_info_table where date_of_admission between %s and %s;")                                 # 1. Total Students enrolled
        sqls.append("select Count(*) from placement_drives_table where drive_date between %s and %s and placement_status='Placed';")       # Total Students Placed
        sqls.append("select count(*) from student_course_batch as s, batches_table as b where b.start_date between %s and %s and b.batch_id = s.batch_id and s.global_cert ='Yes'")     # Total Exams Enrollement
        sqls.append( "select count(distinct(b.batch_id)) from batches_table as b,student_course_batch as s where b.start_date between %s and %s and b.batch_id = s.batch_id;")                                             # 2. Total Batches Added
        sqls.append( "select count(distinct(drive_id)) from placement_drives_table where drive_date between %s and %s;")                   # Total Company Drives
        sqls.append( "select count(*) from placement_drives_table where drive_date between %s and %s;")                                    # Total Interviews Conducted
        sqls.append("select sum(transaction_amt) from transactions_table where transaction_date between %s and %s")                         # Total Income  # Next one is Total Billed
        sqls.append("select sum(total_paid) from payment_table where billing_date between %s and %s")

        # Running all the sql Queries and gathering all the output
        cur = mydb.cursor()
        dates = (startDate, endDate)
        for sql in sqls:
            cur.execute(sql, dates)
            x = cur.fetchall()[0][0]
            if x is None:
                numbers.append(0)
                continue
            numbers.append(x)
        numbers.append(numbers[-1]-numbers[-2])     #This appends the stats for Total Pending # Total Pending = Total Billed - Total Income

        choices = ['Total Students Enrolled', 'Total Students Placed', 'Total Exams Enrolled', 'Total Batches Started', 'Total Company Drives', 'Total Interviews Conducted', 'Total Income', 'Total Billed', 'Total Pending']

        # Setting all the data wre have on the choice_TableWidget
        self.choice_tableWidget.setColumnCount(2) # Columns are Choice And Total
        self.choice_tableWidget.setRowCount(9)    # The rows are up there

        self.choice_tableWidget.setHorizontalHeaderLabels(['Field', 'Total'])   # Setting the headers
        # Go through all the records and make a row for each of them in the table
        for choice, i, num in zip(choices, range(9), numbers):
            self.choice_tableWidget.setItem(i, 0, QTableWidgetItem(choice))
            self.choice_tableWidget.setItem(i, 1, QTableWidgetItem(str(num)))
        #self.choice_tableWidget.setCurrentIndex(0)

    def showDetailTable(self):
        self.detail_tableWidget.clear()
        self.detail_tableWidget.setRowCount(0)
        self.detail_tableWidget.setColumnCount(0)
        choice = self.choice_tableWidget.currentRow() # the index of the selected Row
        #choice = self.choice_tableWidget.item(row_index,0)

        if choice == 0:
            self.totalStudents()
        elif choice == 1:
            self.totalPlaced()
        elif choice == 2:
            self.totalExams()
        elif choice == 3:
            self.totalBatches()
        elif choice == 4:
            self.totalDrives()
        elif choice == 5 :
            self.totalInterviews()
        else:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0,0,QTableWidgetItem('No Details avaliable.'))

    def totalStudents(self):
        sql = "select first_name, middle_name, last_name, date_of_admission from student_info_table where date_of_admission between %s and %s order by date_of_admission desc;"
        cur = mydb.cursor()
        dates = (self.startDate, self.endDate)
        cur.execute(sql, dates)
        data = cur.fetchall()
        print(data)
        if data == []:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0, 0, QTableWidgetItem('No Details avaliable.'))
            return

        ### Setting the Details of the selected Choice
        self.detail_tableWidget.setRowCount(len(data))
        self.detail_tableWidget.setColumnCount(2)
        self.detail_tableWidget.setHorizontalHeaderLabels(['Student Name', 'Date of Admission'])
        for record,i in zip(data, range(len(data))):
            name = " ".join(record[0:3])
            date = record[3].strftime("%d-%m-%y")
            self.detail_tableWidget.setItem(i, 0, QTableWidgetItem(name))
            self.detail_tableWidget.setItem(i, 1, QTableWidgetItem(date))

    def totalPlaced(self):
        sql = "select s.first_name, s.middle_name, s.last_name, c.company_name, p.drive_date from placement_drives_table as p, student_info_table as s, company_table as c where p.drive_date between %s and %s and placement_status='Placed' and p.student_id = s.student_id and p.company_id = c.company_id order by p.drive_date asc;"
        dates = (self.startDate, self.endDate)
        cur = mydb.cursor()
        cur.execute(sql, dates)
        data = cur.fetchall()

        if not data:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0, 0, QTableWidgetItem('No Details avaliable.'))
            return

        ### Setting the Details of the selected Choice
        self.detail_tableWidget.setRowCount(len(data))
        self.detail_tableWidget.setColumnCount(3)
        self.detail_tableWidget.setHorizontalHeaderLabels(['Student Name', 'Company Name', 'Date'])
        for record, i in zip(data, range(len(data))):
            name = " ".join(record[0:3])
            c_name = record[3]
            date = record[4].strftime("%d-%m-%y")
            self.detail_tableWidget.setItem(i, 0, QTableWidgetItem(name))
            self.detail_tableWidget.setItem(i, 1, QTableWidgetItem(c_name))
            self.detail_tableWidget.setItem(i, 2, QTableWidgetItem(date))

    def totalExams(self):
        sql = "select si.first_name, si.middle_name, si.last_name, c.course_name from student_course_batch as s, batches_table as b, student_info_table as si, courses_table as c where b.batch_id = s.batch_id and s.course_id = c.course_id and si.student_id = s.student_id and s.global_cert ='Yes' and b.start_date between %s and %s order by b.start_date asc;"
        dates = (self.startDate, self.endDate)
        cur = mydb.cursor()
        cur.execute(sql, dates)
        data =  cur.fetchall()
        if not data:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0, 0, QTableWidgetItem('No Details avaliable.'))
            return

        self.detail_tableWidget.setRowCount(len(data))
        self.detail_tableWidget.setColumnCount(2)
        self.detail_tableWidget.setHorizontalHeaderLabels(['Student Name', 'Course Name'])
        for record, i in zip(data, range(len(data))):
            name = " ".join(record[0:3])
            course = record[3]
            self.detail_tableWidget.setItem(i, 0, QTableWidgetItem(name))
            self.detail_tableWidget.setItem(i, 1, QTableWidgetItem(course))

    def totalBatches(self):
        sql = "SELECT b.batch_name, b.start_date, count(s.student_id) FROM batches_table as b, student_course_batch as s where start_date between %s and %s and b.batch_id = s.batch_id group by b.batch_id;"
        cur = mydb.cursor()
        dates = (self.startDate, self.endDate)
        cur.execute(sql, dates)
        data = cur.fetchall()
        if not data:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0, 0, QTableWidgetItem('No Details avaliable.'))
            return
        self.detail_tableWidget.setRowCount(len(data))
        self.detail_tableWidget.setColumnCount(3)
        self.detail_tableWidget.setHorizontalHeaderLabels(['Batch Name', 'No of Students','Start Date'])
        for record, i in zip(data, range(len(data))):
            b_name = record[0]
            date = record[1].strftime("%d-%m-%y")
            s_count = record[2]     # No. of students in that batch
            self.detail_tableWidget.setItem(i, 0, QTableWidgetItem(b_name))
            self.detail_tableWidget.setItem(i, 1, QTableWidgetItem(str(s_count)))
            self.detail_tableWidget.setItem(i, 2, QTableWidgetItem(date))

    def totalDrives(self):
        sql = "select c.company_name, p.drive_date, count(p.drive_id) from placement_drives_table as p, company_table as c where p.drive_date between %s and %s and p.company_id = c.company_id group by p.drive_date,c.company_name order by p.drive_date asc;"
        cur = mydb.cursor()
        dates = (self.startDate, self.endDate)
        cur.execute(sql, dates)
        data = cur.fetchall()
        if not data:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0, 0, QTableWidgetItem('No Details avaliable.'))
            return
        self.detail_tableWidget.setRowCount(len(data))
        self.detail_tableWidget.setColumnCount(3)
        self.detail_tableWidget.setHorizontalHeaderLabels(['Drive Company Name', 'No of Students', 'Drive Date'])
        for record, i in zip(data, range(len(data))):
            d_name = record[0]
            date = record[1].strftime("%d-%m-%y")
            s_count = record[2]  # No. of students in that batch
            self.detail_tableWidget.setItem(i, 0, QTableWidgetItem(d_name))
            self.detail_tableWidget.setItem(i, 1, QTableWidgetItem(str(s_count)))
            self.detail_tableWidget.setItem(i, 2, QTableWidgetItem(date))

    def totalInterviews(self):
        sql = "select s.first_name, s.middle_name, s.last_name, count(p.student_id) from placement_drives_table as p, student_info_table as s where drive_date between %s and %s and s.student_id = p.student_id group by p.student_id order by s.first_name;"
        cur = mydb.cursor()
        dates = (self.startDate, self.endDate)
        cur.execute(sql, dates)
        data =  cur.fetchall()
        if not data:
            self.detail_tableWidget.setRowCount(1)
            self.detail_tableWidget.setColumnCount(1)
            self.detail_tableWidget.setHorizontalHeaderLabels(['Message'])
            self.detail_tableWidget.setItem(0, 0, QTableWidgetItem('No Details avaliable.'))
            return
        self.detail_tableWidget.setRowCount(len(data))
        self.detail_tableWidget.setColumnCount(2)
        self.detail_tableWidget.setHorizontalHeaderLabels(['Student Name', 'No of Interviews'])
        for record, i in zip(data, range(len(data))):
            s_name = " ".join(record[0:3])      # Name Of Student
            i_count = record[3]                 # No. of interviews given by that student
            self.detail_tableWidget.setItem(i, 0, QTableWidgetItem(s_name))
            self.detail_tableWidget.setItem(i, 1, QTableWidgetItem(str(i_count)))

    ########## End of Added Code ########


    def retranslateUi(self, report):
        _translate = QtCore.QCoreApplication.translate
        report.setWindowTitle(_translate("report", "MainWindow"))
        self.label.setText(_translate("report", " Report and Statistics"))
        self.label_2.setText(_translate("report", "Start Date:"))
        self.start_dateEdit.setDisplayFormat(_translate("report", "dd/MM/yyyy"))
        self.label_3.setText(_translate("report", "End Date:"))
        self.end_dateEdit.setDisplayFormat(_translate("report", "dd/MM/yyyy"))
        self.ok_Button.setText(_translate("report", "Ok"))
        self.label_4.setText(_translate("report", "Select Record"))
        self.choice_tableWidget.setSortingEnabled(False)
        item = self.choice_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("report", "Choice"))
        item = self.choice_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("report", "Total"))
        self.label_5.setText(_translate("report", "Record Details"))
        self.backHome_Button.setText(_translate("report", "Back Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    report = QtWidgets.QMainWindow()
    ui = Ui_report()
    ui.setupUi(report)
    report.show()
    sys.exit(app.exec_())