class Students:
    increment=1.1
    def __init__(self,fname,lname,rollno,totalmarks):
        self.fname=fname
        self.lname=lname
        self.rollno=rollno
        self.totalmarks=totalmarks
    def increase(self):
        self.totalmarks=Students.increment*self.totalmarks
    @classmethod
    def changeincrement(cls,value):
        cls.increment=value
    @classmethod
    def from_str(cls,string):
        fname,lname,rollno,totalmarks=string.split("-")
        return cls(fname,lname,rollno,totalmarks)
class programmer(Students):
    def __init__(self, fname, lname, rollno, totalmarks,experience,status):
        super().__init__(fname,lname,rollno,totalmarks)
        self.experience=experience
        self.status=status


    pass
bishal=Students("nepal",2,2,2,2)
harry=programmer("harry","jackson",22,23000,4,"married")
print(harry.status)
print(isinstance(bishal,harry))
#magic dundermethods
