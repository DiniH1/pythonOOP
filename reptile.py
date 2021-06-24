# Let's create a class to inherit Animal class
from animal import Animal # if the file is not in the directory the absolute path is need

class Reptile(Animal): # inheriting from Animal class

    def __init__(self):
        super().__init__() # Super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]


    def seek_heat(self):
        return "It's really chilly looking have fun in the sun"

    def hunt(self):
        return "Keep working hard to find food"

    def use_venom(self):
        return " If i have it I will use it"
# Let's create an object of Reptile class
smart_reptile =Reptile()
# print(smart_reptile.breathe()) # breathe method is inherited from Animal class
# print(smart_reptile.hunt()) # hunt() is available in Reptile class
# print(smart_reptile.eat())
# print(smart_reptile.move())
# print(smart_reptile.hunt())

