class Students:
    increment=1.1
    def __init__(self,fname,lname,rollno,totalmarks):
        self.fname=fname
        self.lname=lname
        self.rollno=rollno
        self.totalmarks=totalmarks
    @property
    def getname(self,fname):
        return fname

    @getname.setter
    def getname(self, fname):
        self.fname=fname
    def __add__(self, other):
        return self.totalmarks+other.totalmarks
    def __repr__(self):
        return "Students({},{},{},{})".format(self.fname,self.lname,self.rollno,self.totalmarks)
    def __str__(self):
        return "the name of employee is {}".format(self.fname)
    def increase(self):
        self.totalmarks=Students.increment*self.totalmarks
    @classmethod
    def changeincrement(cls,value):
        cls.increment=value
    @classmethod
    def from_str(cls,string):
        fname,lname,rollno,totalmarks=string.split("-")
        return cls(fname,lname,rollno,totalmarks)

bishal=Students("nepal",2,2,200)
rohan=Students("rohan",2,2,3000)


