class grandparent:
    def __init__(self):
     print("class grandparent")

class parent:
    def __init__(self):
     print("class parent")

class kid(grandparent,parent):
   def __init__(self):
      super().__init__()
      print("I am a kid")

o=kid()