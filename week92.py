
class age_error(Exception):
#    def __init__(self):
#       print("Age error\nAge should be greater than 18:)")
    pass



n=int(input())
if n<18:
    raise age_error("Age should be greater than 18:)")

