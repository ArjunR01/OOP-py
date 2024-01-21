class m:
    def __init__(self,name,age):
        self.m1=name
        self.m2=age

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        new=m(m1,m2)
        return new
        

o1=m(16,18)
o2=m(17,10)

if((o1.m1+o1.m2)>(o2.m1+o2.m2)):
    print("o1 wins")
else:
    print("o2 wins")