""" Kunai pani function banauna:
    def name(arg1,arg2,arg3):




"""
"""1) function to print "hello functions" """
def show():
    print("Hello functions")
show()

"""2) function to print whatever input from user"""
def show(string):
    print(string)
show("bishal")

""" 3) function input from user pass into function and function le print"""
strings=input("Enter any string:")
def stringprinter(string):
    print(string)

stringprinter(strings)

"""4) parameters p,t,r pass in interest vanne function and store in any variable"""
def interest(p,t,r):
    return p*t*r/100
inte=interest(2,3,4)
print(inte)

"""5) scenarios"""
def name():
    print("this is the function")
print(name)
"""Yo case ma name ko function ko memory location dekhaune cha"""
print(name())
"""Yo case ma none dekhaune cha because return type kei chaina"""

"""6) scenarios regarding parameters:"""
def user(name,age):
    print(f"{name}")
    print(age)
# user("bishal")
"""arguments chaio duita but only one deye so it does not work"""
user("bishal",20)
"""it will work"""



"""7) function returning multiple value scenarios"""
def firstusername(first,second):
    return first
    return second
print(firstusername("Sagar","Bhattrai"))

"""function return first matra garcha second return gardaina!!!"""

"""8) scenario 7 ma dui return garna k garne???"""

def bothusername(first,second):
    return [first,second]
arraydata=bothusername("nina","turner")
print(arraydata[0])
print(arraydata[1])


"""9) wap to pass three values: and return 0 place---- sum, 1 place---- difference, 2 place---- product, 3rd place division """

def calculate(x,y):
    sum=x+y
    diff=x-y
    product=x*y
    div=x/y
    return [sum,diff,product,div]
x,y=input("Enter two no:").split(",")
xi=int(x)
yi=int(y)
final=calculate(xi,yi)
print(f"The sum between {xi} abd {yi} is: {final[0]}")
print(f"The difference between {xi} abd {yi} is: {final[1]}")
print(f"The product between {xi} abd {yi} is: {final[2]}")
print(f"The division between {xi} abd {yi} is: {final[3]}")


"""10) student ko name ra roll no print graune if prameter ma roll cha vane print both if roll vayena vane print name only"""

def student(name=None,roll=None):
    if not name==None:
        print(name)
    else:
        print("no value for name")
    if not roll==None:
        print(roll)
    else:
        print("no value for age")
st1=input("Enter name:")
st2=input("Enter roll:")
student(st1)

"""11) three function use : take_value(), calculate(),display()"""
def take_value():
    p=float(input("Enter principle:"))
    t=float(input("Enter time:"))
    r=float(input("Enter rate:"))
    return [p,t,r]
def calculate():
    interestdata=take_value()
    principle=interestdata[0]
    time=interestdata[1]
    rate=interestdata[2]
    return principle*rate*time/100
def display():
    print(calculate())
display()




