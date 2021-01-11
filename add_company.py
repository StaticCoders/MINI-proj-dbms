# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_company.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="amigobong",
    database="bitsfinal"
)

class Ui_AddCompany_Dailog(object):
    def setupUi(self, AddCompany_Dailog):
        AddCompany_Dailog.setObjectName("AddCompany_Dailog")
        AddCompany_Dailog.resize(578, 294)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddCompany_Dailog.sizePolicy().hasHeightForWidth())
        AddCompany_Dailog.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(AddCompany_Dailog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.companyLabel = QtWidgets.QLabel(AddCompany_Dailog)
        self.companyLabel.setScaledContents(True)
        self.companyLabel.setObjectName("companyLabel")
        self.horizontalLayout.addWidget(self.companyLabel)
        self.companyName_Label = QtWidgets.QLineEdit(AddCompany_Dailog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyName_Label.sizePolicy().hasHeightForWidth())
        self.companyName_Label.setSizePolicy(sizePolicy)
        self.companyName_Label.setMaximumSize(QtCore.QSize(800, 40))
        self.companyName_Label.setInputMask("")
        self.companyName_Label.setText("")
        self.companyName_Label.setFrame(True)
        self.companyName_Label.setDragEnabled(False)
        self.companyName_Label.setClearButtonEnabled(True)
        self.companyName_Label.setObjectName("companyName_Label")
        self.horizontalLayout.addWidget(self.companyName_Label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.warningLabel = QtWidgets.QLabel(AddCompany_Dailog)
        self.warningLabel.setEnabled(True)
        self.warningLabel.setStyleSheet("color :rgb(252, 1, 7)")
        self.warningLabel.setObjectName("warningLabel")
        self.horizontalLayout_2.addWidget(self.warningLabel)
        self.addCompany_Button = QtWidgets.QPushButton(AddCompany_Dailog)
        self.addCompany_Button.setDefault(False)
        self.addCompany_Button.setFlat(False)
        self.addCompany_Button.setObjectName("addCompany_Button")
        self.horizontalLayout_2.addWidget(self.addCompany_Button)
        self.cancelButton = QtWidgets.QPushButton(AddCompany_Dailog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(AddCompany_Dailog)
        QtCore.QMetaObject.connectSlotsByName(AddCompany_Dailog)

        ######Added Code#######

        self.warningLabel.hide()  #Hide the Warning Label
        self.addCompany_Button.clicked.connect(self.add_Company)

    def add_Company(self):
        c_name = self.companyName_Label.text().strip() # Taking the Company Name from TextBox
        if len(c_name.strip()) == 0:
            self.warningLabel.setText('Cant Have Empty Field!')
            self.warningLabel.show()
            self.companyName_Label.clear()
            return
        cur = mydb.cursor()
        sql = "select * from company_table where company_name = %s"
        cur.execute(sql,(c_name,))
        if len(cur.fetchall()) == 0: # If there is no company Present witht that name Add it.
            sql_insert = "insert into company_table(company_name) values(%s)"
            cur.execute(sql_insert,(c_name,))
            mydb.commit()
            self.warningLabel.setText('{} added!'.format(c_name)) # Display Comany added in Green Color
            self.warningLabel.setStyleSheet("color : green;")
            self.warningLabel.show()
        else:              # Else show the warning message.
            self.warningLabel.setText('{} Already added present!'.format(c_name))
            self.warningLabel.show()
        self.companyName_Label.clear() # Clear the text in the text Field.
        cur.close() # Close The cursor

    ######End of Added Code#######

    def retranslateUi(self, AddCompany_Dailog):
        _translate = QtCore.QCoreApplication.translate
        AddCompany_Dailog.setWindowTitle(_translate("AddCompany_Dailog", "Add Company"))
        #AddCompany_Dailog.setWindowTitle('Add Company')
        self.companyLabel.setText(_translate("AddCompany_Dailog", "Company Name"))
        self.companyName_Label.setPlaceholderText(_translate("AddCompany_Dailog", "Enter the New Company Name"))
        self.warningLabel.setText(_translate("AddCompany_Dailog", "Name Already Exists!"))
        self.addCompany_Button.setText(_translate("AddCompany_Dailog", "Add Company"))
        self.cancelButton.setText(_translate("AddCompany_Dailog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddCompany_Dailog = QtWidgets.QDialog()
    ui = Ui_AddCompany_Dailog()
    ui.setupUi(AddCompany_Dailog)
    AddCompany_Dailog.show()
    sys.exit(app.exec_())
