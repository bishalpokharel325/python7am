hour,minute,second=input("Enter your call duration in H:M:S = ").split(":")
hour=float(hour)
minute=float(minute)
second=float(second)
call=hour*60+minute+second/60
bonus=0
if hour>60 or minute>60 or second>60:
    print("Error! Please enter correct information.")
else:
    print(f"your total call time is:{minute} minutes.")
    if call<5 and call!=0:
       bonus=3

    if call>=5 and call<10:
       bonus=6

    if call>=10 and call<20:
       bonus=9

    if call>=20 and call<45:
       bonus=20

    if call>=45:
       bonus=10
    print(f"You got bonus of Rs. {bonus}")

