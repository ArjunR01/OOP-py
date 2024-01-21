class python:
    def public(self,name):
        self.name=name
    def private(self,pin):
        self.__pin=pin
    def display(self):
        print(self.name,self.__pin)

o=python()
o.public(2)
o.private(1234)
# print(o.__pin)
# o.private(1234)
o.display()
# print(o.public())