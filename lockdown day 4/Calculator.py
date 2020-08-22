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
