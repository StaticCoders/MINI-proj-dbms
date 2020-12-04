# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDrive.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
####### Added Code #######
import icon
import datetime
from inflect import engine # used to Pluralize words(strings)
from PyQt5.QtWidgets import QMessageBox, QTreeWidgetItem
from PyQt5.QtCore import QDate
import mysql.connector
mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="amigobong",
    database="bitsfinal")

####### End of added Code ######


class Ui_ViewDrive(object):
    def setupUi(self, ViewDrive):
        ViewDrive.setObjectName("ViewDrive")
        ViewDrive.resize(996, 685)
        font = QtGui.QFont()
        font.setPointSize(18)
        ViewDrive.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ViewDrive)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(700, 100))
        self.label.setMaximumSize(QtCore.QSize(700, 100))
        font = QtGui.QFont()
        font.setPointSize(49)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(90, 30))
        self.label_4.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.search_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_comboBox.sizePolicy().hasHeightForWidth())
        self.search_comboBox.setSizePolicy(sizePolicy)
        self.search_comboBox.setMinimumSize(QtCore.QSize(180, 30))
        self.search_comboBox.setMaximumSize(QtCore.QSize(180, 30))
        self.search_comboBox.setObjectName("search_comboBox")
        self.search_comboBox.addItem("")
        self.search_comboBox.addItem("")
        self.search_comboBox.addItem("")
        self.search_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.search_comboBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.search_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_dateEdit.sizePolicy().hasHeightForWidth())
        self.search_dateEdit.setSizePolicy(sizePolicy)
        self.search_dateEdit.setMinimumSize(QtCore.QSize(130, 30))
        self.search_dateEdit.setMaximumSize(QtCore.QSize(130, 30))
        self.search_dateEdit.setCalendarPopup(True)
        self.search_dateEdit.setObjectName("search_dateEdit")
        self.horizontalLayout_3.addWidget(self.search_dateEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(65, 30))
        self.label_2.setMaximumSize(QtCore.QSize(65, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.search_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_LineEdit.setMinimumSize(QtCore.QSize(400, 30))
        self.search_LineEdit.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.search_LineEdit.setFont(font)
        self.search_LineEdit.setClearButtonEnabled(False)
        self.search_LineEdit.setObjectName("search_LineEdit")
        self.horizontalLayout.addWidget(self.search_LineEdit)
        self.search_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.search_Button.sizePolicy().hasHeightForWidth())
        self.search_Button.setSizePolicy(sizePolicy)
        self.search_Button.setMinimumSize(QtCore.QSize(40, 30))
        self.search_Button.setMaximumSize(QtCore.QSize(40, 30))
        self.search_Button.setAutoFillBackground(False)
        self.search_Button.setStyleSheet("background-color : black;")
        self.search_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_Button.setIcon(icon)
        self.search_Button.setObjectName("search_Button")
        self.horizontalLayout.addWidget(self.search_Button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.output_treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_treeWidget.sizePolicy().hasHeightForWidth())
        self.output_treeWidget.setSizePolicy(sizePolicy)
        self.output_treeWidget.setMinimumSize(QtCore.QSize(750, 300))
        self.output_treeWidget.setMaximumSize(QtCore.QSize(750, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output_treeWidget.setFont(font)
        self.output_treeWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.output_treeWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.output_treeWidget.setTabKeyNavigation(False)
        self.output_treeWidget.setProperty("showDropIndicator", True)
        self.output_treeWidget.setAlternatingRowColors(True)
        self.output_treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.output_treeWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.output_treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.output_treeWidget.setAutoExpandDelay(-1)
        self.output_treeWidget.setItemsExpandable(True)
        self.output_treeWidget.setWordWrap(True)
        self.output_treeWidget.setObjectName("output_treeWidget")
        self.output_treeWidget.header().setCascadingSectionResizes(False)
        self.output_treeWidget.header().setDefaultSectionSize(150)
        self.output_treeWidget.header().setMinimumSectionSize(80)
        self.output_treeWidget.header().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.output_treeWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_Button.sizePolicy().hasHeightForWidth())
        self.back_Button.setSizePolicy(sizePolicy)
        self.back_Button.setMinimumSize(QtCore.QSize(140, 50))
        self.back_Button.setMaximumSize(QtCore.QSize(140, 50))
        self.back_Button.setObjectName("back_Button")
        self.horizontalLayout_4.addWidget(self.back_Button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 2, 1, 1, 1)
        ViewDrive.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewDrive)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 22))
        self.menubar.setObjectName("menubar")
        ViewDrive.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewDrive)
        self.statusbar.setObjectName("statusbar")
        ViewDrive.setStatusBar(self.statusbar)

        self.retranslateUi(ViewDrive)
        QtCore.QMetaObject.connectSlotsByName(ViewDrive)

        ################  Added Code ##############
        self.search_dateEdit.setDate(QDate.currentDate())
        sql_company = 'select company_name from company_table'
        sql_name = 'select first_name, middle_name, last_name from student_info_table;'
        cur = mydb.cursor()
        cur.execute(sql_company)
        self.company_names = [x[0] for x in cur.fetchall()]
        cur.execute(sql_name)
        self.student_names = [' '.join(x) for x in cur.fetchall()]

        self.search_dateEdit.hide()
        self.output_treeWidget.clear()
        self.output_treeWidget.setHeaderLabels(['','',''])
        self.search_comboBox.activated.connect(self.dateChange)
        self.search_Button.clicked.connect(self.searchDrive)

    def searchDrive(self):
        # After the search_Button is clicked run this function
        self.choice = self.search_comboBox.currentText() # Get the Choice
        if self.choice == 'Date':
            self.searchViaDate()
        elif self.choice == 'Company Name':
            self.searchViaCompanyName()
        elif self.choice == 'Student Name':
            self.searchViaStudentName()
        elif self.choice == 'Recent':
            self.searchViaRecent()


    def searchViaStudentName(self):
        self.text = self.search_LineEdit.text().strip()  # get the student name typed
        textTuple = tuple(self.text.split())
        cur = mydb.cursor()
        sql = "select distinct(drive_id) from placement_drives_table as p, student_info_table as s where s.first_Name = %s and s.middle_name = %s and s.last_name = %s and s.student_id = p.student_id;"
        cur.execute(sql, textTuple)
        drive_id = cur.fetchall()  # Get the all the drive ids for the given Company
        if len(drive_id) != 0:
            drive_id = [x[0] for x in drive_id]
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("'{}' has not been added to any Company Drive or is not registered".format(self.text))
            msg.exec_()
            return
        cname_lst = []  # List of all the companies the Student has been in
        date_lst = []  # Dates of the drive
        stud_name = self.text  # Makes the full name of the student entered.
        for id in drive_id:
            # All the data is cleaned and stored in the 'data' dictionary for each drive after for loop completes
            sql = "select first_name,middle_name,last_name,company_name,p.drive_date FROM student_info_table as s, company_table as c, placement_drives_table as p where p.drive_id = %s and p.student_id = s.student_id and p.company_id = c.company_id order by p.drive_date desc;"
            cur.execute(sql, (id,))
            res = cur.fetchall()
            cname_lst.append(res[0][3])
            date_lst.append(res[0][4].strftime('%d-%m-%Y'))

        # Now lets display the data on the QtreeWidget
        # First Set the header labels:
        self.output_treeWidget.clear() # Clear the Widget before displaying data
        self.output_treeWidget.setHeaderLabels(['Student Name', 'Date', 'Company Names'])
        # Now lets add all the data
        p = engine() # It is used to pluralize words
        word = str(len(cname_lst)) + " " + p.plural('Company', len(cname_lst))  # automatic plural of 'Company' karne ke liye
        first_row = [stud_name, "", word]
        parent = QTreeWidgetItem(self.output_treeWidget,first_row)  # This is the Main Company record, where we click the drop down
        for company,day in zip(cname_lst,date_lst):
            QTreeWidgetItem(parent, ["",day,company])


    def searchViaCompanyName(self):
        self.text = self.search_LineEdit.text().strip() #get the company name typed
        data = dict()       # The Dictionary where all the data from DB is stored
        sql = "select distinct(drive_id) from placement_drives_table as p, company_table as c where c.company_name = %s and c.company_id = p.company_id;"
        cur = mydb.cursor()
        cur.execute(sql, (self.text,))
        drive_id = cur.fetchall()  # Get the all the drive ids for the given Company
        if len(drive_id) != 0:
            drive_id = [x[0] for x in drive_id]
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No Drives present with the Company Name '{}'".format(self.text))
            msg.exec_()
            return

        for id in drive_id:
            # All the data is cleaned and stored in the 'data' dictionary for each drive after for loop completes
            sql = "select first_name,middle_name,last_name,company_name,p.drive_date FROM student_info_table as s, company_table as c, placement_drives_table as p where p.drive_id = %s and p.student_id = s.student_id and p.company_id = c.company_id order by p.drive_date desc;"

            cur.execute(sql, (id,))
            res = cur.fetchall()
            stud_names = [' '.join(x[:3]) for x in res] # Makes the full name of all students of that drive.
            c_name = res[0][3] # Take the Company Name here
            d_date = res[0][4].strftime('%d-%m-%Y') # The date of the drive
            data[id] = {'Date' : d_date, 'Stud_Names' : stud_names, 'Company_Name' : c_name}

        # Now lets display the data on the QtreeWidget
        # First Set the header labels:
        self.output_treeWidget.clear() # Clear the Widget before displaying data
        self.output_treeWidget.setHeaderLabels(['Company Name', 'Date', 'Student Names'])
        # Now lets add all the data
        p = engine() # It is used to pluralize words
        for key, value in data.items():
            word = str(len(value['Stud_Names']))+" "+p.plural( 'Student', len(value['Stud_Names'])) # automatic plural of 'Student' karne ke liye
            first_row = [value['Company_Name'], value['Date'], word]
            parent = QTreeWidgetItem(self.output_treeWidget, first_row) # This is the Main Company record, where we click the drop down
            for name in value['Stud_Names']:
                QTreeWidgetItem(parent, ["","",name])


    def searchViaRecent(self):
        date = str(datetime.date.today())       # Current Date in string 'yyyy-mm-dd'
        data = dict()

        sql = "select drive_id from placement_drives_table where date_sub(curdate(), interval 30 day) <= drive_date order by drive_date desc;"
        # Takes all the records with date within the last 30 days.
        cur = mydb.cursor()
        cur.execute(sql)
        drive_id = cur.fetchall()  # Get the all the drive ids created for that day
        if len(drive_id) != 0:
            drive_id = [x[0] for x in drive_id]
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No Company Drive for the last 30 Days")
            msg.exec_()
            return
        for id in drive_id:
            # All the data is cleaned and stored in the 'data' dictionary for each drive after for loop completes
            sql = "SELECT first_name,middle_name,last_name,company_name,p.drive_date FROM student_info_table as s, company_table as c, placement_drives_table as p where p.drive_id = %s and p.student_id = s.student_id and p.company_id = c.company_id;"
            cur.execute(sql, (id,))
            res = cur.fetchall()
            stud_names = [' '.join(x[:3]) for x in res] # Makes the full name of all students of that drive.
            c_name = res[0][3] # Take the Company Name here
            d_date = res[0][4].strftime('%d-%m-%Y') # The date of the drive
            data[id] = {'Date' : d_date, 'Stud_Names' : stud_names, 'Company_Name' : c_name}

        # Now lets display the data on the QtreeWidget
        # First Set the header labels:
        self.output_treeWidget.clear() # Clear the Widget before displaying data
        self.output_treeWidget.setHeaderLabels(['Company Name', 'Date', 'Student Names'])
        # Now lets add all the data
        p = engine() # It is used to pluralize words
        for key, value in data.items():
            word = str(len(value['Stud_Names']))+" "+p.plural( 'Student', len(value['Stud_Names'])) # automatic plural of 'Student' karne ke liye
            first_row = [value['Company_Name'], value['Date'], word]
            parent = QTreeWidgetItem(self.output_treeWidget, first_row) # This is the Main Company record, where we click the drop down
            for name in value['Stud_Names']:
                QTreeWidgetItem(parent, ["","",name])


    def searchViaDate(self):
        # This functions displays result according to date
        date = self.search_dateEdit.date().toString('yyyy-MM-dd') # Get the date into a string
        data = dict()         #Dictionary where all the data will be stored data = {'drive_id':{'date':yyyy-mm-dd, names : [...],Company_Name: cname}}
        # Getting all the drive_ids with the given date.
        sql = "select distinct(drive_id) from placement_drives_table where drive_date = %s;"
        cur = mydb.cursor()
        cur.execute(sql, (date,))
        drive_id = cur.fetchall()    # Get the all the drive ids created for that day
        if len(drive_id) != 0:
            drive_id = [x[0] for x in drive_id]
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No Company Drive for given Date")
            msg.exec_()
            return
        for id in drive_id:
            # All the data is cleaned and stored in the 'data' dictionary for each drive after for loop completes
            sql = "SELECT s.first_name,s.middle_name,s.last_name,c.company_name,p.drive_date FROM student_info_table as s, company_table as c, placement_drives_table as p where p.drive_id = %s and p.student_id = s.student_id and p.company_id = c.company_id;"
            cur.execute(sql, (id,))
            res = cur.fetchall()
            stud_names = [' '.join(x[:3]) for x in res] # Makes the full name of all students of that drive.
            c_name = res[0][3] # Take the Company Name here
            d_date = res[0][4].strftime('%d-%m-%Y') # The date of the drive
            data[id] = {'Date' : d_date, 'Stud_Names' : stud_names, 'Company_Name' : c_name}

        # Now lets display the data on the QtreeWidget
        # First Set the header labels:
        self.output_treeWidget.clear() # Clear the Widget before displaying data
        self.output_treeWidget.setHeaderLabels(['Company Name', 'Date', 'Student Names'])
        # Now lets add all the data
        p = engine() # It is used to pluralize words
        for key, value in data.items():
            word = str(len(value['Stud_Names']))+" "+p.plural( 'Student', len(value['Stud_Names'])) # automatic plural of 'Student' karne ke liye
            first_row = [value['Company_Name'], value['Date'], word]
            parent = QTreeWidgetItem(self.output_treeWidget, first_row) # This is the Main Company record, where we click the drop down
            for name in value['Stud_Names']:
                QTreeWidgetItem(parent, ["","",name])


    def createCompleter(self): # sets the QCompleter for the search box
        self.choice = self.search_comboBox.currentText()
        self.lst = []
        if self.choice == 'Company Name':
            self.lst = self.company_names
        elif self.choice == 'Student Name':
            self.lst = self.student_names
        self.completer = QtWidgets.QCompleter(self.lst, self.search_LineEdit)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)  # It will match anythinng. First Name, Last Name, Anything
        self.search_LineEdit.setCompleter(self.completer)


    def dateChange(self):
        # To display or hide the dateEdit box. If date is chosen the it is show else it is hidden.
        if self.search_comboBox.currentText() == 'Date':
            self.search_dateEdit.show()
            self.search_LineEdit.clear()
            self.search_LineEdit.setEnabled(False) # In Date mode, no text should be entered so disabling the text field
        elif self.search_comboBox.currentText() == 'Recent':
            self.search_dateEdit.hide()
            self.search_LineEdit.clear()
            self.search_LineEdit.setEnabled(False) #Disable text box when choice is recent
        else:
            self.search_dateEdit.hide()
            self.search_LineEdit.setEnabled(True)
            self.search_LineEdit.clear()

        self.createCompleter() # Also set the new Completer


    ########## End Of Added Code ##########
    def retranslateUi(self, ViewDrive):
        _translate = QtCore.QCoreApplication.translate
        ViewDrive.setWindowTitle(_translate("ViewDrive", "MainWindow"))
        self.label.setText(_translate("ViewDrive", "View Company Drives"))
        self.label_4.setText(_translate("ViewDrive", "Search  By:"))
        self.search_comboBox.setItemText(0, _translate("ViewDrive", "Company Name"))
        self.search_comboBox.setItemText(1, _translate("ViewDrive", "Student Name"))
        self.search_comboBox.setItemText(2, _translate("ViewDrive", "Date"))
        self.search_comboBox.setItemText(3, _translate("ViewDrive", "Recent"))
        self.search_dateEdit.setDisplayFormat(_translate("ViewDrive", "dd/MM/yyyy"))
        self.label_2.setText(_translate("ViewDrive", "Search:"))
        self.search_LineEdit.setPlaceholderText(_translate("ViewDrive", "Enter Company Name or Student Name"))
        self.output_treeWidget.setSortingEnabled(False)
        self.output_treeWidget.headerItem().setText(0, _translate("ViewDrive", "Company Name"))
        self.output_treeWidget.headerItem().setText(1, _translate("ViewDrive", "Date"))
        self.output_treeWidget.headerItem().setText(2, _translate("ViewDrive", "Students"))
        self.back_Button.setText(_translate("ViewDrive", "Back"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewDrive = QtWidgets.QMainWindow()
    ui = Ui_ViewDrive()
    ui.setupUi(ViewDrive)
    ViewDrive.show()
    sys.exit(app.exec_())
