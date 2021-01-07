# from PyQt5.QtWidgets import QMessageBox

from HomePage import *
from chooseInBatches import *
from chooseInRegistration import *
from batchAllotment import *
from Registration import *
from chooseInSearch import *
from searchInStudent import *
from updateStudentInfo import *
from updateInBatch import *
from chooseInUpdate import *
from UpdateCourse import *
from newTransaction import *
from ListOfTrans import *
from addInstallments import *
from chooseInPayment import *
from searchInBatch import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.batchAllotment = Ui_BatchAllotmentWindow()
        self.batches = Ui_BatchesWindow()
        self.newRegistration = Ui_NewRegistrationWindow()
        self.registration = Ui_RegistrationWindow()
        self.homeScreen = Ui_MainWindow()
        self.searchSection = Ui_SearchWindow()
        self.studentsSection = Ui_StudentsSectionWindow()
        self.searchInBatch = Ui_SearchInBatch()
        self.update = Ui_UpdateWindow()
        self.updateStudentInfo = Ui_UpdateStudentInfo()
        self.updateBatch = Ui_UpdateBatchWindow()
        self.updateCourse = Ui_UpdateCourseWindow()
        self.startHome()

    # HOME

    def startHome(self):
        self.homeScreen.setupUi(self)
        self.setWindowTitle("Home")
        self.homeScreen.registration.clicked.connect(self.startRegistration)
        self.homeScreen.Batches.clicked.connect(self.startBatches)
        self.homeScreen.Search.clicked.connect(self.startSearch)
        self.homeScreen.Update.clicked.connect(self.startUpdate)
        self.homeScreen.Payment.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()
    # REGISTRATION

    def startRegistration(self):
        self.registration.setupUi(self)
        self.setWindowTitle("Registration")
        self.registration.newRegistrationButton.clicked.connect(self.startNewRegistration)
        self.registration.cancelButton.clicked.connect(self.startHome)
        self.hide()
        self.showMaximized()

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

    # SEARCH

    def startSearch(self):
        self.searchSection.setupUi(self)
        self.setWindowTitle("Search")
        self.hide()
        self.showMaximized()
        self.searchSection.backButton.clicked.connect(self.startHome)
        self.searchSection.studentButton.clicked.connect(self.startSearchInStudents)
        self.searchSection.batchButton.clicked.connect(self.startSearchInBatch)

    def startSearchInStudents(self):
        self.studentsSection.setupUi(self)
        self.setWindowTitle("Students Section")
        self.hide()
        self.showMaximized()
        self.studentsSection.cancelButton.clicked.connect(self.startSearch)

    def startSearchInBatch(self):
        self.searchInBatch.setupUi(self)
        self.setWindowTitle("Students Section")
        self.hide()
        self.showMaximized()
        self.searchInBatch.backButton.clicked.connect(self.startSearch)
        self.searchInBatch.backButton_2.clicked.connect(self.startSearch)

    # UPDATE

    def startUpdate(self):
        self.update.setupUi(self)
        self.setWindowTitle("Update Section")
        self.hide()
        self.showMaximized()
        self.update.studentButton.clicked.connect(self.startUpdateStudentInfo)
        self.update.batchButton.clicked.connect(self.startUpdateInBatch)
        self.update.courseButton.clicked.connect(self.startUpdateInCourse)
        self.update.backButton.clicked.connect(self.startHome)

    def startUpdateStudentInfo(self):
        self.updateStudentInfo.setupUi(self)
        self.setWindowTitle("Update Student Info")
        self.hide()
        self.showMaximized()
        self.updateStudentInfo.backButton.clicked.connect(self.startUpdate)

    def startUpdateInCourse(self):
        self.updateCourse.setupUi(self)
        self.setWindowTitle("Update in Courses")
        self.hide()
        self.showMaximized()
        self.updateCourse.backButton.clicked.connect(self.startUpdate)
        self.updateCourse.backButton_2.clicked.connect(self.startUpdate)

    def startUpdateInBatch(self):
        self.updateBatch.setupUi(self)
        self.setWindowTitle("Update In Batch")
        self.hide()
        self.showMaximized()
        self.updateBatch.backButton_2.clicked.connect(self.startUpdate)
        self.updateBatch.backButton_3.clicked.connect(self.startUpdate)
        self.updateBatch.backButton_4.clicked.connect(self.startUpdate)

    def startPayment(self):
        self.payment = Ui_PaymentWindow()
        self.payment.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Payment")
        self.payment.cancelButton.clicked.connect(self.startHome)
        self.payment.installmentButton.clicked.connect(self.addInstallment)
        self.payment.transactionButton.clicked.connect(self.newTransaction)
        self.payment.listTransactionsButton.clicked.connect(self.newListTransaction)
        self.hide()
        self.showMaximized()

    # Add Installment Tab
    def addInstallment(self):
        self.newinstallment = Ui_InstallmentWindow()
        self.newinstallment.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Add Installments")
        # self.newinstallment.addButton.clicked.connect(self.addingInstallment)
        # self.newinstallment.submitButton.clicked.connect(self.submitInstallment)
        self.newinstallment.cancelButton.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()

    # New transaction tab
    def newTransaction(self):
        self.newtransaction = Ui_TransactionWindow()
        self.newtransaction.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("New Transaction")
        self.newtransaction.cancelButton.clicked.connect(self.startPayment)
        # add functions
        self.hide()
        self.showMaximized()

    # List Transaction button call
    def newListTransaction(self):
        self.listTransaction = Ui_ListMainWindow()
        self.listTransaction.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("List Of Transactions")
        self.listTransaction.backButton.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
