# SECTIONS IN THIS FILE
# FUNCTIONS IN REGISTRATION TAB
# FUNCTIONS IN SEARCH TAB
# FUNCTIONS IN BATCHES TAB
# FUNCTIONS IN UPDATE TAB
# FUNCTIONS IN PAYMENT TAB

from PyQt5.QtWidgets import QMessageBox
from Registration import *
from HomePage import *
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
        # self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Home")
        self.homescreen.registration.clicked.connect(self.startRegistration)
        self.hide()
        self.showMaximized()

    def startRegistration(self):
        self.registration = Ui_RegistrationWindow()
        self.registration.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Registration")
        self.registration.closeButton.clicked.connect(self.startHome)
        self.registration.registerButton.clicked.connect(self.register)
        self.hide()
        self.showMaximized()

    # FUNCTIONS IN REGISTERATION TAB

    def register(self):
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
        if fname == "" or mname == "" or lname == "" or phone == "" or address == "" or education == "":
            self.registration.warningLabel.show()
        else:
            tdate = date.today()
            sql = "INSERT INTO student_info (first_name,middle_name,last_name,date_of_admission,phone,address," \
                  "education,experience,referral) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            val = (fname, mname, lname, tdate, phone, address, education, experience, referral)
            mycursor.execute(sql, val)
            if mycursor.rowcount == 1:
                print("Data inserted successfully!")
            else:
                print("Problem occurred while inserting data")
            mydb.commit()
            getid = "select student_id from student_info order by student_id desc limit 1;"
            mycursor.execute(getid)
            result = mycursor.fetchone()
            courseChecked = []
            while self.registration.model.item(i):
                if self.registration.model.item(i).checkState():
                    courseChecked.append(self.registration.model.item(i).text())
                    self.registration.model.item(i).setCheckState(False)
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
        msg.setInformativeText(text)
        x = msg.exec_()
        self.startHome()

    # FUNCTIONS IN SEARCH TAB

    # FUNCTIONS IN BATCHES TAB
    # FUNCTIONS IN UPDATE TAB
    # FUNCTIONS IN PAYMENT TAB


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
