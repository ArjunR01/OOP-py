while(1):
   print("1.Create sets\n2.Union\n3.Intersection\n4.Difference\n5.Symmetric Difference\n6.Equality\n7.Superiority\nEnter your choice:")
   n=int(input())
   match(n):
      case(1):
         set1=set()
         set2=set()
         m=int(input("Enter number of elements you want to enter in set 1:"))
         for i in range(m):
             o=int(input("ENter Element="))
             set1.add(o)
         p=int(input("Enter number of elements you want to enter in set 2:"))
         for i in range(p):
             o=int(input("ENter Element="))
             set2.add(o)
      case(2):
         print(set1.union(set2))
      case(3):
         print(set1.intersection(set2))
      case(4):
         n=int(input("1.A-B or 2.B-A"))
         if(n==1):
            print(set1.difference(set2))
         else:
            print(set2.difference(set1))
      case(5):
         print(set1.symmetric_difference(set2))
      case(6):
         if(set1==set2):
            print("Equal")
         else:
            print("Not equal")
      case(7):
         if(set1>set2):
            print("Set1 is superior")
         else:
            print("set 2 is superior")
      case(0):
         exit()