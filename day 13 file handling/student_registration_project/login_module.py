import csv
from csvtolistconverter import csvtolistconverter
def login():
    open("record.csv","r+")
    data=csvtolistconverter("record.csv")
    user_name=input("Enter User Name:")
    password=input("Enter password:")
    i=0
    checker_username=0
    checker_uandp=0
    return_id=-1
    while i<len(data):
        if user_name==data[i][1]:
            print("User name exist.")
            if(password==data[i][2]):
                print("Login Sucessful")
                print(f"Welcome {data[i][1]}")
                return_id=i+1
            else:
               checker_uandp=checker_uandp+1
        else:
            checker_username=checker_username+1
        i=i+1
    if return_id!=-1:
        data=csvtolistconverter("record.csv")
        print("your Profile Details:")
        print("------------------------------------------")
        print(f"Your Registration id is:{return_id}")
        print("------------------------------------------")
        print(f"Your User name is:{data[return_id - 1][1]}")
        print("------------------------------------------")
        print(f"Your Password is:{data[return_id - 1][2]}")
        print("------------------------------------------")
        print(f"Your email is:{data[return_id - 1][3]}")
        print("------------------------------------------")
        print(f"Your phone no is:{data[return_id - 1][4]}")
        print("------------------------------------------")
    else:
        if(checker_username==0):
            print("Could not find user name")
            login()
        else:
            print("Username exist but password does not match")
            login()
