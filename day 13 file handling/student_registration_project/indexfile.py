from register_module import register
from login_module import login
from csvtolistconverter import csvtolistconverter
import os
import getpass
import csv
"""Check for record.csv and if this file do not exist then it will make a new one"""
if not os.path.exists("record.csv"):
    check_file=open("record.csv","w")
    check_file.close()
"""Change records in csv into list :  data[indexno][data1,2 or 3]"""

data=csvtolistconverter("record.csv")
totalno=len(data)
print(totalno)
"""Input from user whether: they want to register or login"""
print("WELCOME!!!!!!")
print("Choose whether you want to register, login or exit:")
print("Enter 1 to register \nEnter 2 to login \nEnter any other key to exit program")
choose=input("your choice:")
if choose=="1":
    print("This is Registration Page:")
    print("-----------------------------")
    checker=1
    user_name = input("Enter user name:")
    while checker!=0:
        checker=0
        i = 0
        while i < totalno:
            if user_name == data[i][1]:
                print("Username already exist.")
                checker=1
                user_name = input("Please Enter new Username:")

            i = i + 1
    user_password=input("Enter Password:")
    user_repassword=input("Confirm Password:")
    while(user_password!=user_repassword):
        print("Password could not be confirmed:")
        user_password = input("Enter Password:")
        user_repassword = input("Confirm Password:")
    user_email = input("Enter Email:")
    user_phoneno = input("Enter Phone no:")
    """check if username exist or not."""

    if checker==0:
        register(totalno+1,user_name,user_password,user_email,user_phoneno)
    secondchoice=input("Do you want to login? (Y or N)")
    if secondchoice=="Y" or secondchoice=="y":
        login()
    else:
        print("Username already exist. Please Enter new username.")
if choose=="2":
    login()








