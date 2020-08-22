class student:
    increment=1.5
    no_of_students=0
    def __init__(self,fname,lname,address,phone,salary,working_days,leave):
        self.fname=fname
        self.lname=lname
        self.address=address
        self.phone=phone
        self.salary=salary
        self.working_days=working_days
        self.leave=leave
        if self.fname=="neha":
            self.increment=0.5
        student.no_of_students=student.no_of_students+1
    def increase(self):
        self.salary=self.salary*student.increment
    @classmethod
    def change_increment(cls,change_value):
        cls.increment=change_value



print(student.no_of_students)
bishal=student("Bishal","Pokharel","pepsicola","98754685",25000,25,2)
rohan=student("rohan","bhattrai","pepsicola","98754685",35000,25,2)
neha=student("neha","kapoor","pepsicola","98754685",10000,25,2)
print(student.no_of_students)
print(bishal.salary)
bishal.change_increment(2.5)
bishal.increase()
print(bishal.salary)
neha.increase()
print(neha.salary)
