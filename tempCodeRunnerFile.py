class vehicle:
    def general_usage(self):
        print("general usage:transportation")
    
class car(vehicle):
    def __init__(self):
        print("i'm a car")
        self.wheels=4
        self.has_roof=True
    def specific_usage(self):
        print("specific use for:family")
class motorcycle(vehicle):
    def __init__(self):
        print("i'm a motorcycle")
        self.wheels=2
        self.has_roof=False
    def specific_usage(self):
        print("specific use for:personal")

c=car()
c.general_usage()
c.specific_usage()