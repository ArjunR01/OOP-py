class complex:
    def __intit__(self):
        self.real=0
        self.img=0
    def setval(self,r,i):
        self.real=r
        self.img=i
    def __add__(self,other):
        # real=self.real+other.real
        # img=self.img+other.img
        # return (real,img)
        t=complex()
        t.real=self.real+other.real
        t.img=self.img+other.img
        return(t.real)


c1=complex()
c1.setval(1,2)
c2=complex()
c2.setval(2,9)
# c3=c1+c2
print(c1+c2)

