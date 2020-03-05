print("Please Enter following information to know your result:")
name=input("Enter your name:")
count=0
english=float(input("Enter your marks in English (0-100):"))
if english>100:
    print("Secured Marks cannot be greater than 100.")
    english = float(input("Enter your marks in English (0-100):"))
math=float(input("Enter your marks in Math (0-100):"))
if math>100:
    print("Secured Marks cannot be greater than 100.")
    math = float(input("Enter your marks in Math (0-100):"))
science=float(input("Enter your marks in Science (0-100):"))
if science>100:
    print("Secured Marks cannot be greater than 100.")
    english = float(input("Enter your marks in Science (0-100):"))
computer=float(input("Enter your marks in Computer (0-100):"))
if computer>100:
    print("Secured Marks cannot be greater than 100.")
    nepali = float(input("Enter your marks in computer (0-100):"))
nepali=float(input("Enter your marks in Nepali (0-100):"))
if nepali>100:
    print("Secured Marks cannot be greater than 100.")
    english = float(input("Enter your marks in Nepali (0-100):"))
if english>100 or math>100 or science>100 or computer>100 or nepali>100:
    print("!!!!!error!!!!")
    print("Please enter your marks correctly.")
else:
    total=english+math+science+computer+nepali
    average=total/5
    print(f"Your total marks is:{total}")
    print(f"Your average marks is:{average}")
    if english>32 and math>32 and science>32 and computer>32 and nepali>32:
        print("Congratulations! You have passed in every subjects.")
        if average>=32 and average<45:
            print("Your have secured third division.")
        elif average>=45 and average<60:
            print("Your have secured second division.")
        elif average>=60 and average<75:
            print("You have sucured first division.")
        else:
            print("You have secured distinction.")
    else:

        print("Sorry! You have failed in following subjects:")
        if english<32:
            print("English")
            count=count+1
        if math<32:
            print("Math")
            count=count+1
        if science<32:
            print("Science")
            count=count+1
        if computer<32:
            print("Computer")
            count=count+1
        if nepali<32:
            print("nepali")
            count=count+1
            print(f"You have failed in {count} subjects.")



