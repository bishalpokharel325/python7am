# class Mobile:
#     def __init__(self,name):
#         self.name=name
#     def mobilename(self):
#         return f'I am {self.name}'
#
# class Nokia(Mobile):
#     def __init__(self,name,price):
#         #constructr ma child le parante ko kura lai ni call garnu parxa
#         #duita tarika le garna sakincha
#         # #1. init and yesari kaam garindaina
#         # Mobile.__init__(self.name)
#         # pass
#         #2 super garera garne
#         super().__init__(name)
#         # self.price=price
# #parent ra child ma inherent caste huncha example
# obj=Nokia("Nokiaa",2000)
# print(obj.mobilename())
# #forcefully call garna mildaina
# #inheret garnu paryo
# #main bujne kura yo ho
# #parent vako feature lai child herule lene
# #check garne tarika
# print(isinstance(obj,Mobile))
# print(issubclass(Nokia,Mobile))
# print(issubclass(Mobile,Nokia))
class Mobile:
    __price=200
    def __init__(self,price):
        self.__price=price
    def getprice(self):
        return self.__price

obj=Mobile(40000)
print(obj.__price)
#protected pani aucha kura
#_ single hypen dera garna milxa
# tinta garne ... public: sapai class le lina sakcha , __private: within class,_protected: child class le ni run garna sakcha,__specialmethod__ or __dundermethod__
#tinwoda scope chai bujnu parcha natra pubnlic mai badi kam hucnha
#voli gayera kaam gardai jada kheri.. class DB vanera banaye, connnecton lai chai out of class call nai nagros,
#task multiple inhertience
#class nokia le mobile ra brand duai ko le inherent garne banaune
#object lai __add__ method garen
class Students:
    def __init__(self,price):

        pass
obj=Students("ram",2000)
obj1=Students("sita",20000)