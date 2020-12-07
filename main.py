# SECTIONS IN THIS FILE
# FUNCTIONS IN REGISTRATION TAB
# FUNCTIONS IN SEARCH TAB
# FUNCTIONS IN BATCHES TAB
# FUNCTIONS IN UPDATE TAB
# FUNCTIONS IN PAYMENT TAB

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Registration import *
from HomePage import *
from chooseInBatches import *
from chooseInRegistration import *
from batchAllotment import *
from Registration import *
# For Company Drives
from AddCompanyDrive_Final import *     # To add a drive
from add_company import *               # To add a company
from viewDrive import *                 # To view the drive
from CompanyDriveMain import *          # The main window to show the options for Company Drive
from report import *                    # To show the report tab
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amigobong",
    database="bitsfinal"
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.report = Ui_report()
        self.viewdrive = Ui_ViewDrive()
        self.addcompany  = Ui_AddCompany_Dailog()
        self.addcompanydrive  = Ui_AddDrive()
        self.companyDrive = Ui_ComanyDriveMain()
        self.batchAllotment = Ui_BatchAllotmentWindow()
        self.batches = Ui_BatchesWindow()
        self.newRegistration = Ui_NewRegistrationWindow()
        self.registration = Ui_RegistrationWindow()
        self.homescreen = Ui_MainWindow()
        self.startHome()

    # HOME

    def startHome(self):
        self.homescreen.setupUi(self)
        self.setWindowTitle("Home")
        self.homescreen.registration.clicked.connect(self.startRegistration)
        self.homescreen.Batches.clicked.connect(self.startBatches)
        self.homescreen.companydrives.clicked.connect(self.startCompanyDrives)
        self.homescreen.pushButton_5.clicked.connect(self.startReport)
        self.hide()
        self.showMaximized()

    # REGISTRATION

    def startRegistration(self):
        self.registration.setupUi(self)
        self.setWindowTitle("Registration")
        self.registration.newRegistrationButton.clicked.connect(self.startNewRegistration)
        self.registration.cancelButton.clicked.connect(self.startHome)
        self.hide()
        self.showMaximized()  # maxmizes the Window

    def startNewRegistration(self):
        self.newRegistration.setupUi(self)
        self.setWindowTitle("New Registration")
        self.newRegistration.cancelButton.clicked.connect(self.startRegistration)
        self.hide()
        self.showMaximized()

    # BATCHES

    def startBatches(self):
        self.batches.setupUi(self)
        self.setWindowTitle("Batches")
        self.hide()
        self.showMaximized()
        self.batches.addBatchButton.clicked.connect(self.batches.addBatch)
        self.batches.allotBatchButton.clicked.connect(self.startBatchAllotment)
        self.batches.cancelButton.clicked.connect(self.startHome)

    def startBatchAllotment(self):
        self.batchAllotment.setupUi(self)
        self.hide()
        self.showMaximized()
        self.batchAllotment.cancelButton.clicked.connect(self.startBatches)
    def startCompanyDrives(self):   # This is open the Window of Company Drive with the options
        self.companyDrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Company Drives")
        self.companyDrive.addDrive_Button.clicked.connect(self.addCompanyDrive)
        self.companyDrive.addCompany_Button.clicked.connect(self.addCompany)
        self.companyDrive.viewDrive_Button.clicked.connect(self.viewDriveCall)
        self.companyDrive.backHome_Button.clicked.connect(self.startHome)
        self.hide()
        self.showMaximized()

    # COMPANY DRIVES

    def addCompanyDrive(self):   # This will open the Add Drive Window
        self.addcompanydrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.addcompanydrive.cancel_Button.clicked.connect(self.startCompanyDrives) # if he clicks cancel while adding Drive go back to CompanyDrive  main

    def addCompany(self):  #This show the dialog box to add Company Name to Company List
        self.x = QtWidgets.QDialog()
        self.addcompany.setupUi(self.x)
        self.addcompany.cancelButton.clicked.connect(self.x.hide)
        self.x.show()

    def viewDriveCall(self):   # This Shows all the existing Company Drives.
        self.viewdrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.viewdrive.back_Button.clicked.connect(self.startCompanyDrives)

    # REPORT AND STATS

    def startReport(self):
        self.report.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.report.backHome_Button.clicked.connect(self.startHome)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
