# SECTIONS IN THIS FILE
# FUNCTIONS IN REGISTRATION TAB
# FUNCTIONS IN SEARCH TAB
# FUNCTIONS IN BATCHES TAB
# FUNCTIONS IN UPDATE TAB
# FUNCTIONS IN PAYMENT TAB

from PyQt5.QtWidgets import QMessageBox

from Registration import *
from HomePage import *
# For Company Drives
from AddCompanyDrive_Final import *     # To add a drive
from add_company import *               # To add a company
from viewDrive import *                 # To view the drive
from CompanyDriveMain import *          # The main window to show the options for Company Drive
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
        self.startHome()

    # ALL THE MAIN TABS

    def startHome(self):
        self.homescreen = Ui_MainWindow()
        self.homescreen.setupUi(self)
        # self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Home")
        self.homescreen.registration.clicked.connect(self.startRegistration)
        self.homescreen.companydrives.clicked.connect(self.startCompanyDrives)
        self.hide()
        self.showMaximized()

    def startRegistration(self):
        # Starts the Registration tab.
        self.registration = Ui_RegistrationWindow()
        self.registration.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Registration")
        self.registration.closeButton.clicked.connect(self.startHome) 
        self.registration.registerButton.clicked.connect(self.register)  # Start the new student register Tab
        self.hide()
        self.showMaximized()  # maxmizes the Window

    # FUNCTIONS IN REGISTERATION TAB

    def register(self):


        # Get the text from all the text  Boxes
        fname = self.registration.fNameIp.text()
        mname = self.registration.mNameIp.text()
        lname = self.registration.lNameIp.text()
        phone = self.registration.phoneIp.text()
        address = self.registration.addressIp.toPlainText()
        education = self.registration.educationIp.text()
        experience = self.registration.experienceIp.text()
        referral = self.registration.referralIp.text()
        i = 0
        result = ()
        mycursor = mydb.cursor()

        # To check if any of the Text fields were Empty. If yes display a error message in the label hid.
        if fname == "" or mname == "" or lname == "" or phone == "" or address == "" or education == "":
            self.registration.warningLabel.show()
        else:
            tdate = date.today()
            sql = "INSERT INTO student_info_table (first_name,middle_name,last_name,phone,whatsapp,email,date_of_admission,address," \
                  "education,experience,referral) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            val = (fname, mname, lname, tdate, phone, address, education, experience, referral)
            mycursor.execute(sql, val) # insert all the values taken to the database
            if mycursor.rowcount == 1:
                print("Data inserted successfully!")
            else:
                print("Problem occurred while inserting data")
            mydb.commit()
            getid = "select student_id from student_info order by student_id desc limit 1;"
            mycursor.execute(getid)
            result = mycursor.fetchone()     # Fetch the StudentID of latest Student entered.
            courseChecked = []               # All the courses selected will be appended in this list
            while self.registration.model.item(i):
                if self.registration.model.item(i).checkState():     # if the course was checked
                    courseChecked.append(self.registration.model.item(i).text())
                    self.registration.model.item(i).setCheckState(False)  # Uncheck the course items 
                i += 1
            i = 0
            for x in courseChecked:
                sql = "SELECT course_id FROM courses WHERE course_name = \"" + x + "\""
                mycursor.execute(sql)
                courseid = mycursor.fetchone()
                sql = "INSERT INTO student_batch_course(student_id, course_id) VALUES(%s,%s)"
                val = (result[0], courseid[0])
                mycursor.execute(sql, val)
                if mycursor.rowcount == 1:
                    print("Data inserted successfully!")
                else:
                    print("Problem occurred while inserting data")
                mydb.commit()

                # Clear all the fields after taking the data
                self.registration.fNameIp.clear()
                self.registration.mNameIp.clear()
                self.registration.lNameIp.clear()
                self.registration.phoneIp.clear()
                self.registration.addressIp.clear()
                self.registration.educationIp.clear()
                self.registration.experienceIp.clear()
                self.registration.referralIp.clear()

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Successful")
        msg.resize(800, 800)
        msg.setStyleSheet("QMessageBox{background-color: rgb(0,0,0);, color: white;}")
        msg.setText("Registration Successful")
        text = "StudentID: " + str(result[
                                       0]) + "\nName: " + fname + " " + mname + " " + lname + "\nPhone: " + phone + "\nAddress: " + address + "\nEducation: " + education + "\nExperience: " + experience + "\nReferred By: " + referral
        msg.setInformativeText(text) # A dialog box that displays the information of the student added
        x = msg.exec_()
        self.startHome()

    def startCompanyDrives(self):   # This is open the Window of Company Drive with the options
        self.companyDrive = Ui_ComanyDriveMain()
        self.companyDrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Company Drives")
        self.companyDrive.addDrive_Button.clicked.connect(self.addCompanyDrive)
        self.companyDrive.addCompany_Button.clicked.connect(self.addCompany)
        self.companyDrive.viewDrive_Button.clicked.connect(self.viewDriveCall)
        self.companyDrive.backHome_Button.clicked.connect(self.startHome)
        self.hide()
        self.showMaximized()

    def addCompanyDrive(self):   # This will open the Add Drive Window
        self.addcompanydrive  = Ui_AddDrive()
        self.addcompanydrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.addcompanydrive.cancel_Button.clicked.connect(self.startCompanyDrives) # if he clicks cancel while adding Drive go back to CompanyDrive  main

    def addCompany(self):  #This show the dialog box to add Company Name to Company List
        self.addcompany  = Ui_AddCompany_Dailog()
        self.x = QtWidgets.QDialog()
        self.addcompany.setupUi(self.x)
        self.addcompany.cancelButton.clicked.connect(self.x.hide)
        self.x.show()

    def viewDriveCall(self):   # This Shows all the existing Company Drives.
        self.viewdrive = Ui_ViewDrive()
        self.viewdrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.viewdrive.back_Button.clicked.connect(self.startCompanyDrives)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
