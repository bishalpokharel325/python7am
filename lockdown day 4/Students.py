#class ko name ra file ko name autai banauda ramro
#class vaneko blueprint ho..
#Class kasari crate garne
#Methods and properties
#init confusingkuraho
#init special method ho
#parameter kasari set garne init ko? .. suppose student register form banaudaicham,,, student lai call hunebitkai k rakhne/?? name class form.. automatic nai required garnu paro vane init use garne
# class Students:
#     def __init__(self,name):
#         #important kura... function ma return garincha... but init ma return type hunna.. afai return hunxa
#
#         print("Hello Python")
#     x=10
#     #yo class ko property
#     def test(self):
#         print(self.x)
#         #x value lai access garna self use garne students.x or self.x duai garna milxa
#         return 'I am methods'
#     def getfulname(self):

    #yo method ho

#class vitra ayo vane method class bahira ayo vane function vanxa
#self default nai install hunxa
#Property and Method
obj=Students()
#hamile instatious banaim
print(obj)
#() paranthesis narakheni hunxa
#parameter cha vane chai rakhdahuncha natra narakheni hunxa
print(obj.name())
# print(x) garna painexaina
obj=Students().x
#rule: obj=Students()
obj=Students()
print(obj.x)
#self le kunai pani argument accept gardaina
#JAVAscript java ma this vanne keyword rakhincheo
#but python ma self vanekai students ho
#self.x garna paincha
#ekdum important kura ho yo chai
#global x rakhera ni garna milxa
#attribute and behavior
#yetinai ho OOPS..
#main concept chai yei ho.. encapsulation cha aru k k cha
#every class ma init vanne function huncha this isimportant
#constructor ho init
# init vako kura heru automatically run huncha

class Calculator:

    def takevalue(self, p, t, r):
        self.p = p
        self.t = t
        self.r = r
        pass

    def calvalue(self):
        self.result = (self.p*self.t*self.r)/100
        pass

    def display(self):
        return f'simple interest is {self.result}'
        pass

    pass

obj = Calculator()
obj.takevalue(500,8,10)
obj.calvalue()
print(obj.display())