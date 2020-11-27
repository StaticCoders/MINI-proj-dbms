
from PyQt5.QtWidgets import QMessageBox
from HomePage import *
from chooseInBatches import *
from chooseInRegistration import *
from batchAllotment import *
from Registration import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.startHome()

    # HOME

    def startHome(self):
        self.homescreen = Ui_MainWindow()
        self.homescreen.setupUi(self)
        self.setWindowTitle("Home")
        self.homescreen.registration.clicked.connect(self.startRegistration)
        self.homescreen.Batches.clicked.connect(self.startBatches)
        self.homescreen.Payment.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()

    # REGISTRATION

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

    # BATCHES

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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
