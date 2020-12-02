# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListOfTrans.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransactionMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 841)
        MainWindow.setStyleSheet("\n"
"background-color: #212121;\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_title_label = QtWidgets.QLabel(self.centralwidget)
        self.list_title_label.setMinimumSize(QtCore.QSize(300, 50))
        self.list_title_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.list_title_label.setFont(font)
        self.list_title_label.setObjectName("list_title_label")
        self.verticalLayout.addWidget(self.list_title_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_recent = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_recent.setMinimumSize(QtCore.QSize(0, 50))
        self.radioButton_recent.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_recent.setFont(font)
        self.radioButton_recent.setStyleSheet("color: rgb(238, 238, 238);")
        self.radioButton_recent.setChecked(True)
        self.radioButton_recent.setObjectName("radioButton_recent")
        self.horizontalLayout.addWidget(self.radioButton_recent)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.radioButton_daily = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_daily.setMinimumSize(QtCore.QSize(0, 50))
        self.radioButton_daily.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_daily.setFont(font)
        self.radioButton_daily.setStyleSheet("color: rgb(238, 238, 238);")
        self.radioButton_daily.setObjectName("radioButton_daily")
        self.horizontalLayout.addWidget(self.radioButton_daily)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listView_input = QtWidgets.QListView(self.centralwidget)
        self.listView_input.setMinimumSize(QtCore.QSize(900, 0))
        self.listView_input.setMaximumSize(QtCore.QSize(900, 16777215))
        self.listView_input.setStyleSheet("\n"
"border: 3px solid #0d7377;\n"
"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"\n"
"\n"
"")
        self.listView_input.setObjectName("listView_input")
        self.verticalLayout.addWidget(self.listView_input)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(140, 50))
        self.backButton.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton#backButton{\n"
"                                       color: #eeeeee;\n"
"                                        background-color: #212121;\n"
"                                        border: 2px solid #9a0002;\n"
"                                        border-radius: 25px;\n"
"                                        }\n"
"                                  \n"
"QPushButton#backButton:hover{\n"
"border: 3px solid rgb(255, 0, 0);\n"
" background-color: #9a0002;\n"
"                                        }")
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.list_title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#32e0c4;\">List Of Transactions</span></p></body></html>"))
        self.radioButton_recent.setText(_translate("MainWindow", "Recent Top 100"))
        self.radioButton_daily.setText(_translate("MainWindow", "Daily Transactions"))
        self.backButton.setText(_translate("MainWindow", "Back"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
