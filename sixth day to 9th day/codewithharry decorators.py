"""Decorators modify functionality of function."""

"""1. function can be assigned into another variable which itself act as a function"""
def funct1(x,y):
    print(x+y)
funct2=funct1
funct2(5,6)

"""2. function lai assigned garisakexi org funct lai delete garda will funct2 also get deleted?"""
def funct3(x,y):
    print(x-y)
funct4=funct3
del funct3
funct4(2,3)

"""3) function lai pani return garna sakincha.......
write a program to define function and input function to be executed according to input of user
"""
def sum(x,y):
    return x+y
def diff(x,y):
    return x-y
def product(x,y):
    return x*y
def division(x,y):
    return x/y
x=float(input("Enter frst no:"))
y=float(input("Enter second no:"))
userchoice=input("Enter operation you want to perform in these parameters(sum/diff/product/division):")
def functionreturner(choice):
    if choice=="sum":
        return sum
    elif choice=="diff":
        return diff
    elif choice =="product":
        return product
    elif choice=="division":
        return division
    else:
        return print
funct5=functionreturner(userchoice)
result=funct5(x,y)
print(result)


"""4) function lai pani argument ko rup ma lina milcha
WAP to take any function as argument, print starting the function at begining and print ended after exectution of function
"""
def progress(function):
    def inner():
        print("Starting of the function")
        function()
        print("End of the function")
    return inner
def printer():
    print("in progress.......")
printer=progress(printer)
printer()

""""5) no 4 nai decorater ho
this can be done in similar way before defining any function

"""
def progress1(function):
    def inner():
        print("Starting no 2")
        function()
        print("ending no 2")
    return inner
@progress1
def printer1():
    print("in prgress no 2")
printer1()


"""6) WAP to create a function which takes two values a and b and will divide largest and smallest no for decorators and normal one asewell"""
def smart_divider(funct):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return funct(a,b)
        else:
            return funct(a,b)
    return inner
@smart_divider
def diff2(x,y):
    print(x-y)
diff2(2,3)
diff2(3,2)




