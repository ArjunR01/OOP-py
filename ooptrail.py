# class is a design or blueprint
class oop:

    channel="Naga Sai tutorial"
    # __init__ or any ohter functions are methods 
    def config(self):
        print("i5,16GB")
    
    # special function 
    def __init__(self):
        print("inint function")

    @classmethod
    def info(cls):
        return cls.channel

# o1 is in built class by ourselves
o1=oop()

# type 1 for calling a function 
oop.config(o1)

# type 2 for calling  
o1.config()

print(oop.info())