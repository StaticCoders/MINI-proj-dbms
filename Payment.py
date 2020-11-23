import mysql.connector
from Payment.py import *
from NewTransaction.py import *

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="tanvi7102",
    database="mpdev"
)