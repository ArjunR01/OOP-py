class sum:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        self.num=self.num+other.num
        return self.num
    
o1=sum(2)
o2=sum(3)
print(o1.__add__(o2))