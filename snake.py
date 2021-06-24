# Lets create a class called Snake

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True


# Let's add some specific methods/behaviours
    def use_tongue_to_smell(self):
        return "If i can touch it I can smell it"
# Let's create an object of Snake class
smart_snake = Snake()

# print(smart_snake.move()) # move() from Animal class
# print(smart_snake.hunt()) # hunt() is available from Reptile class
# print(smart_snake.use_tongue_to_smell()) # from current class



