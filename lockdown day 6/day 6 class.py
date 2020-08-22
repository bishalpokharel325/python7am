#decorator ko kura heru hernu ??
#static method ra classmethod huncha yaha
#property decorator: purai method lai nai property banauna milcha.. method lai property banaune
#property decorator: method lai property ma change garne ho
#prop thichne for getter and setter

class Mobile:
    def __init__(self, name):
        self.name = name
    # @property
    # def mobilename(self):
    #     return f' Mobile name is {self.name}'
    @classmethod
    def mobilename(cls):
        cls.name="ram"
    @staticmethod
    def getname():
        pass



obj=Mobile("Nokia")
print(obj.mobilename)