# SECTIONS IN THIS FILE
# FUNCTIONS IN REGISTRATION TAB
# FUNCTIONS IN SEARCH TAB
# FUNCTIONS IN BATCHES TAB
# FUNCTIONS IN UPDATE TAB
# FUNCTIONS IN PAYMENT TAB

from PyQt5.QtWidgets import QMessageBox
from Registration import *
from HomePage import *
from chooseInBatches import *
from chooseInPayment import *
from chooseInRegistration import *
from AddInstallments import *
from addNewBatch import *
from batchAllotment import *
from Registration import *
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="mpdev"
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.startHome()

    # ALL THE MAIN TABS

    def startHome(self):
        self.homescreen = Ui_MainWindow()
        self.homescreen.setupUi(self)
        self.setWindowTitle("Home")
        self.homescreen.registration.clicked.connect(self.startRegistration)
        self.homescreen.Batches.clicked.connect(self.startBatches)
        self.homescreen.Payment.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()

    def startRegistration(self):
        self.registration = Ui_RegistrationWindow()
        self.registration.setupUi(self)
        self.setWindowTitle("Registration")
        self.registration.newRegistrationButton.clicked.connect(self.startNewRegistration)
        self.registration.cancelButton.clicked.connect(self.startHome)
        self.hide()
        self.showMaximized()

    def startNewRegistration(self):
        self.newregistration = Ui_NewRegistrationWindow()
        self.newregistration.setupUi(self)
        self.setWindowTitle("New Registration")
        self.newregistration.cancelButton.clicked.connect(self.startRegistration)
        self.hide()
        self.showMaximized()

    def startBatches(self):
        self.batches = Ui_BatchesWindow()
        self.batches.setupUi(self)
        self.setWindowTitle("Batches")
        self.hide()
        self.showMaximized()
        self.batches.addBatchButton.clicked.connect(self.batches.addBatch)
        self.batches.allotBatchButton.clicked.connect(self.startBatchAllotment)
        self.batches.cancelButton.clicked.connect(self.startHome)

    def startBatchAllotment(self):
        self.batchAllotment = Ui_BatchAllotmentWindow()
        self.batchAllotment.setupUi(self)
        self.hide()
        self.showMaximized()
        self.batchAllotment.cancelButton.clicked.connect(self.startBatches)


    def startPayment(self):
        self.payment = Ui_PaymentWindow()
        self.payment.setupUi(self)
        self.setWindowTitle("Payment")
        self.payment.cancelButton.clicked.connect(self.startHome)
        self.payment.installmentButton.clicked.connect(self.startInstallments)
        self.hide()
        self.showMaximized()

    def startInstallments(self):
        self.installment = Ui_InstallmentWindow()
        self.installment.setupUi(self)
        self.setWindowTitle("Installments")
        self.hide()
        self.showMaximized()

    # FUNCTIONS IN REGISTERATION TAB

    # def register(self):
    #     registered = self.registration.registerStudent()
    #     if registered:
    #         self.startHome()

    # FUNCTIONS IN SEARCH TAB

    # FUNCTIONS IN BATCHES TAB
    # FUNCTIONS IN UPDATE TAB
    # FUNCTIONS IN PAYMENT TAB


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
