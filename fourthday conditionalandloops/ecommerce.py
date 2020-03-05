print("------------WELCOME TO E-COMMERCE WEBSITE----------")
print("Here are our products and their selling prices:")
print("SN     Products     Price")
print("---------------------------\n")
print("1      Dell        50000")
print("2      Mac         150000")
print("3      Tosiba      65000")
print("----------------------------")
"""!Defining no of different quantities of products user want to buy in three variables."""
dell=int(input("Enter no. of dell laptops you want to buy:"))
mac=int(input("Enter no. of Mac laptops you want to buy:"))
tosiba=int(input("Enter no. of Tosiba laptops you want to buy:"))
subtotal=dell*50000+mac*150000+tosiba*65000
location=input("Enter your address (ktm/bkt/ltp):")
deliverycharge=0
packcost=0
taxamount=0
total=0
grandtotal=0
if location=="ktm" or location=="bkt" or location=="ltp":
    print("For making a purchase, You can choose two options:")
    print("1. Either to be delivered at home.")
    print("2. Or your will pick up the product yourself.")
    print("Note: our home delivery charge is Rs. 1000")
    print("Do you want to your products to be delivered at home? (Y or N)")
    choice=input()
    if choice=="Y" or choice=="y":
        deliverycharge=1000
    print("Our packaging services:")
    print("----------------------------")
    print("1. normal packaging: Rs. 1000")
    print("2. Packaging with laptop bags: Rs. 2500")
    print("3. packaging as gift: Rs. 5000")
    print("---------------------------")
    packaging=int(input("Enter your packaging option(1/2/3):"))
    if packaging==1:
        packcost=1000
    if packaging==2:
        packcost=2500
    if packaging==3:
        packcost=5000
    total=subtotal+deliverycharge+packcost
    if location=="ktm":
        taxamount=0.13*total
    grandtotal=total+taxamount
    print("Your cost details:")
    print("----------------------------------------------------------------------------")
    print("SN     Description     quantity    rate           amount           Remarks")
    print("----------------------------------------------------------------------------")
    print(f"1      Dell              {dell}          50000           {dell*50000}     ")
    print(f"2      Mac               {mac}          150000          {mac*150000}      ")
    print(f"3      Tosiba            {tosiba}          65000           {tosiba * 65000}      ")
    print("--------------------------------------------------------------------------")
    print(f"                        Sub-Total:                 Rs.{subtotal}")
    print(f"                        packaging fees:            Rs.{packcost}")
    print(f"                        delivery charges:          Rs.{deliverycharge}")
    print(f"                        Total Cost:                Rs.{total}")
    print(f"                        VAT(13% of total):         Rs.{taxamount}")
    print(f"------------------------------------------------------------------------")
    print(f"                        Grand Total:               Rs.{grandtotal}")
    print("-------------------------------------------------------------------------")
else:
    print("Sorry, Our service is limited only in kathmandu valley.")


