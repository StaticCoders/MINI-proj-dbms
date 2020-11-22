# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewTransaction.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewPayment(object):
    def setupUi(self, NewPayment):
        NewPayment.setObjectName("NewPayment")
        NewPayment.resize(1297, 858)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        NewPayment.setFont(font)
        NewPayment.setStyleSheet("QMainWindow{\n"
"background-color: #212121;\n"
"}\n"
"QLineEdit {\n"
"background: #eeeeee;\n"
"padding-left: 6px;\n"
"padding-right: 6px;\n"
"border: 2px solid #0d7377;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 3px solid #32e0c4;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color:#eeeeee;\n"
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
"background-color:#eeeeee;\n"
"border: 2px solid #32e0c4;\n"
"selection-background-color: #0d7377;\n"
"}\n"
"\n"
"QTextEdit {\n"
"background: #eeeeee;\n"
"padding-left: 6px;\n"
"padding-right: 6px;\n"
"border: 2px solid #0d7377;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"border: 3px solid #32e0c4;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(NewPayment)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.new_transaction_label = QtWidgets.QLabel(self.centralwidget)
        self.new_transaction_label.setMinimumSize(QtCore.QSize(340, 50))
        self.new_transaction_label.setObjectName("new_transaction_label")
        self.verticalLayout_4.addWidget(self.new_transaction_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setMinimumSize(QtCore.QSize(70, 50))
        self.name_label.setMaximumSize(QtCore.QSize(70, 50))
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setMinimumSize(QtCore.QSize(250, 50))
        self.nameEdit.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet("")
        self.nameEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameEdit.setClearButtonEnabled(True)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.amt_label = QtWidgets.QLabel(self.centralwidget)
        self.amt_label.setMinimumSize(QtCore.QSize(70, 50))
        self.amt_label.setMaximumSize(QtCore.QSize(70, 50))
        self.amt_label.setObjectName("amt_label")
        self.horizontalLayout_2.addWidget(self.amt_label)
        self.amountEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.amountEdit.setMinimumSize(QtCore.QSize(250, 50))
        self.amountEdit.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.amountEdit.setFont(font)
        self.amountEdit.setStyleSheet("")
        self.amountEdit.setClearButtonEnabled(True)
        self.amountEdit.setObjectName("amountEdit")
        self.horizontalLayout_2.addWidget(self.amountEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setMinimumSize(QtCore.QSize(70, 50))
        self.date_label.setMaximumSize(QtCore.QSize(70, 50))
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_3.addWidget(self.date_label)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setMinimumSize(QtCore.QSize(250, 50))
        self.dateEdit.setMaximumSize(QtCore.QSize(250, 50))
        self.dateEdit.setStyleSheet("background-color: rgb(13, 115, 119);\n"
"")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(5, 520))
        self.label.setStyleSheet("background-color: rgb(50, 224, 196);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mode_label = QtWidgets.QLabel(self.centralwidget)
        self.mode_label.setMinimumSize(QtCore.QSize(180, 50))
        self.mode_label.setMaximumSize(QtCore.QSize(180, 50))
        self.mode_label.setObjectName("mode_label")
        self.horizontalLayout_4.addWidget(self.mode_label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(250, 50))
        self.comboBox.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.remark_label = QtWidgets.QLabel(self.centralwidget)
        self.remark_label.setMinimumSize(QtCore.QSize(80, 50))
        self.remark_label.setMaximumSize(QtCore.QSize(80, 50))
        self.remark_label.setObjectName("remark_label")
        self.verticalLayout.addWidget(self.remark_label)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(400, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.installment_num = QtWidgets.QLabel(self.centralwidget)
        self.installment_num.setMinimumSize(QtCore.QSize(400, 50))
        self.installment_num.setMaximumSize(QtCore.QSize(400, 50))
        self.installment_num.setObjectName("installment_num")
        self.verticalLayout_3.addWidget(self.installment_num)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(130, 50))
        self.backButton.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton{\n"
"color: rgb(255, 0, 0);\n"
"border: 2px solid #9a0002;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 3px solid rgb(255, 0, 0);\n"
"background-color: #9a0002;\n"
"\n"
"}\n"
"\n"
"")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_5.addWidget(self.backButton)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        self.label_4.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setMinimumSize(QtCore.QSize(130, 50))
        self.submitButton.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("QPushButton{\n"
"border: 2px solid #0d7377;\n"
"border-radius:20px;\n"
"    color: rgb(50, 224, 196);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 3px solid #32e0c4;\n"
"background-color: #0d7377;\n"
"\n"
"}\n"
"")
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_5.addWidget(self.submitButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem11, 2, 1, 1, 1)
        NewPayment.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewPayment)
        self.statusbar.setObjectName("statusbar")
        NewPayment.setStatusBar(self.statusbar)

        self.retranslateUi(NewPayment)
        QtCore.QMetaObject.connectSlotsByName(NewPayment)

    def retranslateUi(self, NewPayment):
        _translate = QtCore.QCoreApplication.translate
        NewPayment.setWindowTitle(_translate("NewPayment", "New Payment"))
        self.new_transaction_label.setText(_translate("NewPayment", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#32e0c4;\">New Transaction</span></p></body></html>"))
        self.name_label.setText(_translate("NewPayment", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Name:</span></p></body></html>"))
        self.nameEdit.setPlaceholderText(_translate("NewPayment", "    Enter Name"))
        self.amt_label.setText(_translate("NewPayment", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#eeeeee;\">Amount:</span></p></body></html>"))
        self.amountEdit.setPlaceholderText(_translate("NewPayment", "    Enter Amount"))
        self.date_label.setText(_translate("NewPayment", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#eeeeee;\">Date:</span></p></body></html>"))
        self.dateEdit.setDisplayFormat(_translate("NewPayment", "dd-MM-yyyy"))
        self.mode_label.setText(_translate("NewPayment", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#eeeeee;\">Mode of Transaction:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("NewPayment", "Cash"))
        self.comboBox.setItemText(1, _translate("NewPayment", "Cheque"))
        self.comboBox.setItemText(2, _translate("NewPayment", "GooglePay"))
        self.comboBox.setItemText(3, _translate("NewPayment", "Paytm"))
        self.comboBox.setItemText(4, _translate("NewPayment", "Other"))
        self.remark_label.setText(_translate("NewPayment", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#eeeeee;\">  Remark:</span></p></body></html>"))
        self.installment_num.setText(_translate("NewPayment", "<html><head/><body><p><span style=\" font-size:14pt; color:#eeeeee;\">Installment Number : </span></p></body></html>"))
        self.backButton.setText(_translate("NewPayment", "Back"))
        self.submitButton.setText(_translate("NewPayment", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewPayment = QtWidgets.QMainWindow()
    ui = Ui_NewPayment()
    ui.setupUi(NewPayment)
    NewPayment.show()
    sys.exit(app.exec_())
