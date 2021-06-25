# Let's create an Animal class

class Animal: # follow the correct naming convention
    # we need to initialize with built in method called __init__(self)
    # self refers to current class
    def __init__(self): # we declare attributes in our last init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive! "

    def eat(self):
        return "Time to eat "

    def move(self):
        return "move left and right to stay awake "
# We need to create an obkect of this class in order to use any methods
cat = Animal()  # Creating an object of Animal class
# for cat as auser the functionality inside Animal class and the method to breathe is abstracted
# print(cat.breathe())
# print(cat.eat())
print(cat.move())
# Let's move onto our step two