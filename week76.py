d=dict()
e=dict()
while(1):   
   print("1.create dictionary\n2.Enter student details\n3.Delete student Details\n4.Display student marks\n5.Sort student marks based on average\nEnter your choice=")
   n=int(input())
   match(n):
      case(1):
         print("Creating dictionary :)")
         n=int(input("Enter length of dictionary="))
         for i in range(n):
            l=list()
            a=input("Enter student name")
            l.clear()
            for j in range(5):
               z=int(input("Enter student marks one by one="))
               l.append(z)
            s=sum(l)/5
            e[a]=s
            d[a]=l
            del l
      case(2):
         a=input("Enter student name you want to enter=")
         l=list()
         for j in range(5):
            z=int(input("Enter marks="))
            l.append(z)
         d[a]=l
         s=sum(l)/5
         e[a]=s
         del l
      case(3):
         a=input("Enter name of student you want to delete=")
         b=d.keys()
         if(a in b ):
            print(a," is deleted")
            del d[a]
            del e[a]
         else:
            print("Name is not in dictionary")
      case(4):
         print("Student details=")
         print(d)
      case(5):
         print("Marks according to average after sorting are...")
         print(sorted(e.items(), key=lambda item: item[1]))
   print("\n")