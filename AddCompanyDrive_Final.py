# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCompanyDrive2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#####Added Code#####
from CompanyDriveMain import *
from PyQt5.QtCore import QDate  # used for the DateWidget
# Completer for LineEdit and a MessageBox
from PyQt5.QtWidgets import QCompleter, QMessageBox
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amigobong",
    database="db01"
)
#####End of Added Code######


class Ui_AddDrive(object):
    def setupUi(self, AddDrive):
        AddDrive.setObjectName("AddDrive")
        AddDrive.resize(895, 640)
        self.centralwidget = QtWidgets.QWidget(AddDrive)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_label.sizePolicy().hasHeightForWidth())
        self.header_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(41)
        self.header_label.setFont(font)
        self.header_label.setScaledContents(True)
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.gridLayout.addWidget(self.header_label, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.company_label = QtWidgets.QLabel(self.centralwidget)
        self.company_label.setScaledContents(True)
        self.company_label.setObjectName("company_label")
        self.horizontalLayout.addWidget(self.company_label)
        self.comanyName_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comanyName_lineEdit.sizePolicy().hasHeightForWidth())
        self.comanyName_lineEdit.setSizePolicy(sizePolicy)
        self.comanyName_lineEdit.setObjectName("comanyName_lineEdit")
        self.horizontalLayout.addWidget(self.comanyName_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.companyWarning_label = QtWidgets.QLabel(self.centralwidget)
        self.companyWarning_label.setEnabled(True)
        self.companyWarning_label.setText("")
        self.companyWarning_label.setObjectName("companyWarning_label")
        self.verticalLayout.addWidget(self.companyWarning_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.studentName_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentName_lineEdit.sizePolicy().hasHeightForWidth())
        self.studentName_lineEdit.setSizePolicy(sizePolicy)
        self.studentName_lineEdit.setObjectName("studentName_lineEdit")
        self.horizontalLayout_3.addWidget(self.studentName_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.nameSuggestion_list = QtWidgets.QListWidget(self.centralwidget)
        self.nameSuggestion_list.setTabKeyNavigation(False)
        self.nameSuggestion_list.setDragEnabled(True)
        self.nameSuggestion_list.setDragDropOverwriteMode(False)
        self.nameSuggestion_list.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.nameSuggestion_list.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.nameSuggestion_list.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.nameSuggestion_list.setObjectName("nameSuggestion_list")
        self.verticalLayout_2.addWidget(self.nameSuggestion_list)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.nameAdded_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameAdded_list.sizePolicy().hasHeightForWidth())
        self.nameAdded_list.setSizePolicy(sizePolicy)
        self.nameAdded_list.setDragEnabled(True)
        self.nameAdded_list.setDragDropOverwriteMode(False)
        self.nameAdded_list.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.nameAdded_list.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.nameAdded_list.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.nameAdded_list.setObjectName("nameAdded_list")
        self.verticalLayout_4.addWidget(self.nameAdded_list)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.addDrive_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDrive_Button.sizePolicy().hasHeightForWidth())
        self.addDrive_Button.setSizePolicy(sizePolicy)
        self.addDrive_Button.setCheckable(False)
        self.addDrive_Button.setDefault(True)
        self.addDrive_Button.setObjectName("addDrive_Button")
        self.horizontalLayout_6.addWidget(self.addDrive_Button)
        self.cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_Button.sizePolicy().hasHeightForWidth())
        self.cancel_Button.setSizePolicy(sizePolicy)
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout_6.addWidget(self.cancel_Button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 2, 1, 1, 1)
        AddDrive.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddDrive)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 22))
        self.menubar.setObjectName("menubar")
        AddDrive.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddDrive)
        self.statusbar.setObjectName("statusbar")
        AddDrive.setStatusBar(self.statusbar)

        self.retranslateUi(AddDrive)
        QtCore.QMetaObject.connectSlotsByName(AddDrive)

        ###### Added Code ########

        # Variable Nomenclature below
        '''dateEdit-> The input dateWidget
        comanyName_LineEdit -> The input box for the company Name
        companyWarning_label -> The label that comes up if Comapny Name is empty or Not Present
        studentName_lineEdit -> the input box where the student name is typed to search
        nameSuggestion_list -> ListWidget where all the Suggestions for Student Names are displayed as the user types something
        nameAdded_list -> ListWidget where all the added students are dropped to'''

        # Set the default date to current date
        self.dateEdit.setDate(QDate.currentDate())
        # Adding a completer to the Company LineEdit Box
        cur = mydb.cursor()
        # Taking all the Comany_Names for QCompleter
        sql = "select Company_Name from Company;"
        cur.execute(sql)
        lst = cur.fetchall()  # lst will store the names of all the Companies
        if len(lst) != 0:
            lst = [x[0] for x in lst]  # Getting rid of the tuples in the list
        else:
            lst = []
        completer = QCompleter(lst, self.comanyName_lineEdit)
        self.comanyName_lineEdit.setCompleter(
            completer)  # The Completer Set here
        self.companyWarning_label.hide()
        # editingFinished means when he deselects the box of hits enter key
        self.comanyName_lineEdit.editingFinished.connect(self.companyCheck)
        self.studentName_lineEdit.textChanged.connect(self.showNameSuggestions)
        self.addDrive_Button.clicked.connect(self.addDrive)

    def companyCheck(self):
        #Checks if the Company entered is added to the system or not
        # Capitalize() Capitalizes the First letter of the text.
        c_name = self.comanyName_lineEdit.text().capitalize()

        cur = mydb.cursor()
        sql = "select * from Company where Company_Name = %s"
        cur.execute(sql, (c_name,))
        if len(cur.fetchall()) == 0:
            self.companyWarning_label.setText('Company Name Not Added!')
            self.companyWarning_label.setStyleSheet('color:red')
            self.companyWarning_label.show()
            self.comanyName_lineEdit.clear()
        else:
            self.companyWarning_label.hide()
        cur.close()

    def showNameSuggestions(self):
        # Updates eveythime the user changes text in the Student Name LineEdit
        # Shows all suggestions for the name typed from the Database into the QlistView
        stud_Name = self.studentName_lineEdit.text()
        cur = mydb.cursor()
        # The below sql quesry searches if the name matches either first, middle or last name
        sql = "SELECT first_name,middle_name,last_name FROM Student_info WHERE first_name LIKE '%{}%' or middle_name LIKE  '%{}%' or last_name LIKE '%{}%'".format(
            stud_Name, stud_Name, stud_Name)
        cur.execute(sql)
        lst = cur.fetchall()
        if len(lst) != 0:
            # Basically Create a full Name 'First_name Middle_name Last_name' and store that name in lst
            lst = [' '.join(x) for x in lst]
        else:
            lst = []
        # Clear the list of previous suggestions.
        self.nameSuggestion_list.clear()
        # Adds all the items in the list to the QlistWidget
        # We can add all the items in alist to the QlistWidget using .addItems(lst) in one go
        self.nameSuggestion_list.addItems(lst)

    def addDrive(self):
        # Adds the data collected to the database
        c_name = self.comanyName_lineEdit.text().strip()  # Name of the Company
        inp_date = self.dateEdit.date().toString(
            'yyyy-MM-dd')  # has the date(yyyy-mm-dd)
        names_lst = []  # will store the names of all the added Students
        if self.nameAdded_list.count() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No Student Name Added ")
            msg.exec_()
            return
        else:
            for i in range(self.nameAdded_list.count()-1):
                # all the items in AddedNames_list is in the List
                names_lst.append(self.nameAdded_list.item(i).text())
            # Store them as list of name tuples as(First_Name, Middle_Name,Last_Name)
            names_lst = [tuple(name.split()) for name in names_lst]
        if len(c_name) == 0:  # if no company was added and save was clicked
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No Company Name!")
            msg.exec_()
        sql_cid = "select Company_Id from Company where Company_Name = %s"
        sql_sid = "select StudId from Student_info where first_name = %s and middle_name = %s and last_name = %s"
        sql_insert = "insert into Placement(StudID,Company_Id,Date) values(%s,%s,%s)"
        cur = mydb.cursor()
        cur.execute(sql_cid, (c_name,))
        cid = cur.fetchone()[0]  # the company id corresponding to that name
        sid_lst = []  # all the StudId will be stored in this list
        for name in names_lst:  # go through all the names and fetch their StudIds
            cur.execute(sql_sid, name)
            sid_lst.append(cur.fetchone()[0])
        #print(names_lst)
        #print(sid_lst)
        for stud_id in sid_lst:  # insert all the data into the Placement Table for every Student
            cur.execute(sql_insert, (stud_id, cid, inp_date))
        mydb.commit()
        cur.close()
        # to display all the data was added to the DataBases Succesfully.
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Company Drive Added!")
        msg.exec_()

        # Clear all the input widgets after Adding Drive
        self.comanyName_lineEdit.clear()
        self.studentName_lineEdit.clear()
        self.nameSuggestion_list.clear()
        self.nameAdded_list.clear()
        return


    ###### End if Added Code #########

    def retranslateUi(self, AddDrive):
        _translate = QtCore.QCoreApplication.translate
        AddDrive.setWindowTitle(_translate("AddDrive", "Add Company Drive"))
        self.header_label.setText(_translate("AddDrive", "Add Company Drive"))
        self.company_label.setText(_translate("AddDrive", "Enter Company Name"))
        self.label.setText(_translate("AddDrive", "Date"))
        self.dateEdit.setDisplayFormat(_translate("AddDrive", "dd/MM/yyyy"))
        self.label_2.setText(_translate("AddDrive", "Make sure all the students are registered."))
        self.label_3.setText(_translate("AddDrive", "Search Candidate Name"))
        self.label_5.setText(_translate("AddDrive", "Drag and Drop Names from below"))
        self.nameSuggestion_list.setSortingEnabled(True)
        self.label_4.setText(_translate("AddDrive", "Added Students"))
        self.nameAdded_list.setSortingEnabled(True)
        self.addDrive_Button.setText(_translate("AddDrive", "Add Company Drive"))
        self.cancel_Button.setText(_translate("AddDrive", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddDrive = QtWidgets.QMainWindow()
    ui = Ui_AddDrive()
    ui.setupUi(AddDrive)
    AddDrive.show()
    sys.exit(app.exec_())
