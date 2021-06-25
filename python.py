# Let's create Python class

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True


    def digest_large_prey(self):
        return "I can digest anything without chewing"

    def climb(self):
        return "up we go......."

    def sheds_skin(self):
        return "I'm growing out of my skin"


fast_python = Python()
# print(fast_python.climb())
# print(fast_python.hunt())
# print(fast_python.move())
# print(fast_python.use_tongue_to_smell())
# print(fast_python.sheds_skin())
print(fast_python.sheds_skin()) # __ can be used to hide a method (encapsulation)
print(fast_python.)