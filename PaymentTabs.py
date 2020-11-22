# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaymentTabs.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Payment_Window(object):
    def setupUi(self, Payment_Window):
        Payment_Window.setObjectName("Payment_Window")
        Payment_Window.resize(1157, 807)
        Payment_Window.setStyleSheet("QMainWindow{\n"
"background-color: #212121;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: #ffffff;\n"
"border: 2px solid #0d7377;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 3px solid #32e0c4;\n"
"background-color: #0d7377;}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Payment_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstPayment = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstPayment.sizePolicy().hasHeightForWidth())
        self.firstPayment.setSizePolicy(sizePolicy)
        self.firstPayment.setMinimumSize(QtCore.QSize(430, 200))
        self.firstPayment.setMaximumSize(QtCore.QSize(430, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.firstPayment.setFont(font)
        self.firstPayment.setStyleSheet("")
        self.firstPayment.setObjectName("firstPayment")
        self.verticalLayout.addWidget(self.firstPayment)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.newPayment = QtWidgets.QPushButton(self.centralwidget)
        self.newPayment.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newPayment.sizePolicy().hasHeightForWidth())
        self.newPayment.setSizePolicy(sizePolicy)
        self.newPayment.setMinimumSize(QtCore.QSize(430, 200))
        self.newPayment.setMaximumSize(QtCore.QSize(430, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.newPayment.setFont(font)
        self.newPayment.setStyleSheet("")
        self.newPayment.setObjectName("newPayment")
        self.verticalLayout.addWidget(self.newPayment)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.transactionHistory = QtWidgets.QPushButton(self.centralwidget)
        self.transactionHistory.setMinimumSize(QtCore.QSize(430, 200))
        self.transactionHistory.setMaximumSize(QtCore.QSize(430, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.transactionHistory.setFont(font)
        self.transactionHistory.setStyleSheet("")
        self.transactionHistory.setObjectName("transactionHistory")
        self.horizontalLayout.addWidget(self.transactionHistory)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.baclButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baclButton.sizePolicy().hasHeightForWidth())
        self.baclButton.setSizePolicy(sizePolicy)
        self.baclButton.setMinimumSize(QtCore.QSize(125, 45))
        self.baclButton.setMaximumSize(QtCore.QSize(125, 45))
        self.baclButton.setStyleSheet("QPushButton{\n"
"color:rgb(255, 0, 0);\n"
"background-color: ;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;\n"
"border: 2px solid  rgb(255, 0, 0);\n"
"height: 40;\n"
"width:120;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 3px solid rgb(255, 0, 0);\n"
"background-color: #9a0002;\n"
"}\n"
"")
        self.baclButton.setObjectName("baclButton")
        self.horizontalLayout.addWidget(self.baclButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)
        Payment_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Payment_Window)
        self.statusbar.setObjectName("statusbar")
        Payment_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Payment_Window)
        QtCore.QMetaObject.connectSlotsByName(Payment_Window)

    def retranslateUi(self, Payment_Window):
        _translate = QtCore.QCoreApplication.translate
        Payment_Window.setWindowTitle(_translate("Payment_Window", "Payment_Window"))
        self.firstPayment.setText(_translate("Payment_Window", "First Transaction "))
        self.newPayment.setText(_translate("Payment_Window", "New Payment"))
        self.transactionHistory.setText(_translate("Payment_Window", "Transaction History"))
        self.baclButton.setText(_translate("Payment_Window", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Payment_Window = QtWidgets.QMainWindow()
    ui = Ui_Payment_Window()
    ui.setupUi(Payment_Window)
    Payment_Window.show()
    sys.exit(app.exec_())
