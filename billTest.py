from billGenerator import *

# data is the dictionary with all the data that is required for generating a bill receipt.
# All the values of the dictionary should be string. Make sure all values passed are converted to string.
data = { 'Name': 'Jack Sparrow',
         'Phone': '8087032795',
         'Batch': 'RHEL7OCT',
         'Date': '21-12-2020',
         'Tid': '21',
         'Iid':'321',
         'Ino': '3',
         'Cname':'Linux RHEL 7',
         'mode': 'Cash',
         'amount_paid': '15000',
         'total_pending': '35000',
         'total_paid': '20000',
         'next_idate': '12-01-2021'}

bill = BillGenerator()   # Creating a instance of BillGenerator
bill.billGen(data)       # Passing the dictionary to billGen Function