# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(1103, 735)
        LoginPage.setStyleSheet("background-color: qconicalgradient(cx:0.818, cy:0, angle:0, stop:0.568182 rgba(0, 160, 187, 255), stop:0.954545 rgba(255, 0, 75, 255));")
        LoginPage.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(LoginPage)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(LoginPage)
        self.frame.setMaximumSize(QtCore.QSize(431, 401))
        self.frame.setStyleSheet("QToolButton{\n"
"background:#11f0f0;\n"
"border-radius:40px\n"
" }\n"
"\n"
"QFrame{\n"
"background:#2a2a2a;\n"
" }\n"
"\n"
"QLineEdit{\n"
"background:#2a2a2a;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:#B4C6C5;\n"
"border-radius:16px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 120, 101, 41))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(170, 10, 91, 91))
        self.toolButton.setStyleSheet("image: url(:/img/profileimg.png);")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/profileimg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(120, 126))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 210, 311, 41))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 280, 311, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Dialog"))
        self.label.setText(_translate("LoginPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">LOGIN HERE</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("LoginPage", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("LoginPage", "Password"))
        self.pushButton.setText(_translate("LoginPage", "ENTER"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QDialog()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
