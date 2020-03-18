""""""
# print(10/0)
"yo garda "
try:
    print(10/0)
except Exception as e:
    print(e)
finally:
    print("done")
    """finally use vayena vane print hunna"""
"""from calculator import add cha ra add function duiai cha vane as garna skaincha
from calculator import add as add_object
"""
"""afnai error banauna"""
def add(x,y):
    if y==0:
        return "y is zero"
    return x+y


"""if raise not used then"""
try:
    print(add(1,0))
except Exception as e:
    print(e)


"""actual garnae tiarika"""
def add(x,y):
    if y==0:
        raise Exception("y is zeor")
    return x/y
try:
    add(20,0)
except Exception as error:
    print(error)

"""os error, filenot found error, div error, io error, they are inbuilt errors"""

